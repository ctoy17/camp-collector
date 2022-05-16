from django.shortcuts import render
from django.http import HttpResponse
from .models import Camp

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
    return render(request, 'campgrounds/details.html', {'camp':camp})