import os
import boto3
import uuid
from dataclasses import field
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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

def campgrounds_index(request):
    """
    campgrounds view
    http://localhost:8000/campgrounds/
    """
    logging.info("calling campgrounds_index")
    camps = Camp.objects.all()
    return render(request, 'campgrounds/index.html', { 'camps': camps })

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

def add_agency(request, camp_id):
    form = AgencyForm(request.POST)
    if form.is_valid():
        new_agency = form.save(commit=False)
        new_agency.camp_id = camp_id
        new_agency.save()
    return redirect('detail', camp_id=camp_id)

def assoc_features(request, camp_id, features_id):
    Camp.objects.get(id=camp_id).features.add(features_id)
    return redirect('detail', camp_id=camp_id)

def unassoc_features(request, camp_id, features_id):
    Camp.objects.get(id=camp_id).features.remove(features_id)
    return redirect('detail', camp_id=camp_id)

class CampCreate(CreateView):
    model = Camp
    fields = ['name', 'city', 'state', 'pet_friendly']
    success_url = '/campgrounds/'

class CampUpdate(UpdateView):
    model = Camp
    fields = ['name', 'pet_friendly']
    success_url = '/campgrounds/'

class CampDelete(DeleteView):
    model = Camp
    success_url = '/campgrounds/'

class FeaturesList(ListView):
    model = Features

class FeaturesDetail(DetailView):
    model = Features

class FeaturesCreate(CreateView):
    model = Features
    fields = '__all__'

class FeaturesUpdate(UpdateView):
    model = Features
    fields = '__all__'

class FeaturesDelete(DeleteView):
    model = Features
    success_url = '/features/'