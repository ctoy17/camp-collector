from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User





ORGANIZATIONS = (
    ('N', 'National Park'),
    ('S', 'State Park'),    
    ('P', 'Private'),
    ('B', 'Boondock'),
)
# ACTIVITIES = (
#     ('21', "Wildlife Viewing"),
#     ('22', 'Hunting'),
#     ('23', 'Swimming'),
#     ('24', 'Fishing'),
#     ('25', 'Hiking'),
#     ('26', 'Biking'),
#     ('27', 'Climbing'),
#     ('28', 'Horse Riding'),
#     ('29', 'ATV Trail'),
#     ('30', 'Water Sports'),
#     ('31', 'Boating'),
#     ('32', 'Guided Nature Walks'),
#     ('33', 'Backpacking'),
#     ('34', 'Stargazing'),
# )
# AMENITIES = (
#     ('1', "Privacy"),
#     ('2', 'Fire Pit'),
#     ('3', 'Picnic Table'),
#     ('4', 'Flush Toilets'),
#     ('5', 'Cell Sevice'),
#     ('6', 'Accessible'),
#     ('7', 'Dump Station'),
#     ('8', 'Showers'),
#     ('9', 'Food Locker'),
#     ('10', 'Vault Toilet'),
#     ('11', 'Picnic Areas'),
# )
# SITES = (
#     ('T', 'Tent'),
#     ('C', 'Camper'),
#     ('X', 'Cabin'),
#     ('E', 'Electric'),
#     ('NE', 'Non Electric')
# )
# Create your models here.
class Features(models.Model):
    activities = models.CharField(max_length=1000)
    # amenities = models.CharField(max_length=100,  choices=AMENITIES, 
    #     default=[0][0])
    # sites = models.CharField(max_length=100, choices=SITES, 
    #     default=[0][0])

    def get_absolute_url(self):
        return reverse('features_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.activities


class Camp(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pet_friendly = models.BooleanField()
    features = models.ManyToManyField(Features)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'camp_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for camp_id: {self.camp_id} @{self.url}"

class Agency(models.Model):
    organization = models.CharField(
        max_length=1, 
        choices=ORGANIZATIONS, 
        default=ORGANIZATIONS[0][0]
    )
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_organization_display()}"

