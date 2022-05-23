import os
import boto3
import uuid
from dataclasses import field
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Camp, Features, Photo
from .forms import AgencyForm

import logging
logging.basicConfig(level=logging.DEBUG)




# Create your views here.
def home(request):
    """
    home view
    http://localhost:8000/
    """
    return render(request, 'home.html')


def about(request):
    """
    about view
    http://localhost:8000/about/
    """
    #if you have a folder inside the template dir then  use 'folder_name/about.html'
    return render(request, 'about.html')

@login_required
def campgrounds_index(request):
    """
    campgrounds view
    http://localhost:8000/campgrounds/
    """
    logging.info("calling campgrounds_index")
    camps = Camp.objects.all()
    return render(request, 'campgrounds/index.html', { 'camps': camps })

@login_required
def campground_detail(request, camp_id):
    """
    campground detail
    http://localhost:8000/campgrounds/1/
    """
    logging.info('calling camp_info')
    camp = Camp.objects.get(id=camp_id)
    features_camp_doesnt_have = Features.objects.exclude(id__in = camp.features.all().values_list('id'))
    agency_form = AgencyForm()
    return render(request, 'campgrounds/details.html', {'camp':camp, 'agency_form': agency_form, 'features': features_camp_doesnt_have})

@login_required
def add_photo(request, camp_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, camp_id=camp_id)

        except:
            print('An error occurred while uploading to s3')
    return redirect("detail", camp_id=camp_id)

@login_required
def add_agency(request, camp_id):
    form = AgencyForm(request.POST)
    if form.is_valid():
        new_agency = form.save(commit=False)
        new_agency.camp_id = camp_id
        new_agency.save()
    return redirect('detail', camp_id=camp_id)

@login_required
def assoc_features(request, camp_id, features_id):
    Camp.objects.get(id=camp_id).features.add(features_id)
    return redirect('detail', camp_id=camp_id)

@login_required
def unassoc_features(request, camp_id, features_id):
    Camp.objects.get(id=camp_id).features.remove(features_id)
    return redirect('detail', camp_id=camp_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class CampCreate(LoginRequiredMixin, CreateView):
    model = Camp
    fields = ['name', 'city', 'state', 'pet_friendly']
    success_url = '/campgrounds/'
    
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class CampUpdate(LoginRequiredMixin, UpdateView):
    model = Camp
    fields = ['name', 'pet_friendly']
    success_url = '/campgrounds/'

class CampDelete(LoginRequiredMixin, DeleteView):
    model = Camp
    success_url = '/campgrounds/'

class FeaturesList(LoginRequiredMixin, ListView):
    model = Features

class FeaturesDetail(LoginRequiredMixin, DetailView):
    model = Features

class FeaturesCreate(LoginRequiredMixin, CreateView):
    model = Features
    fields = '__all__'

class FeaturesUpdate(LoginRequiredMixin, UpdateView):
    model = Features
    fields = '__all__'

class FeaturesDelete(LoginRequiredMixin, DeleteView):
    model = Features
    success_url = '/features/'