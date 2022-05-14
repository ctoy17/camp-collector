from django.shortcuts import render
from django.http import HttpResponse


import logging
logging.basicConfig(level=logging.DEBUG)

class Camp:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, city, state, activities, pet_friendly):
        self.name = name
        self.city = city
        self.state = state
        self.activities = activities
        self.pet_friendly = pet_friendly

camps = [
    Camp('Watchman Campground', 'Zion National Park', 'Utah', 'Biking, Hiking, Camping, Photography, Star Gazing, Swimming', True),
    Camp('Mather Campground', 'Grand Canyon National Park', 'Arizona', 'Wildlife Viewing, Horse Camping, Star Gazing, Photography, Hiking, Biking', True),
    Camp('Kirk Creek', 'Big Sur', 'California', 'Wildlife Viewing, Hiking, Boating, Water Sports, Fishing, Biking, Hunting', True)
]

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
    return render(request, 'campgrounds/index.html', { 'camps': camps })