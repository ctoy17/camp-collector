from django.db import models

# Create your models here.
class Camp(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    activities = models.TextField(max_length=500)
    pet_friendly = models.BooleanField()