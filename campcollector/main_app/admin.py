from django.contrib import admin
from .models import Agency, Camp, Features, Photo
# Register your models here.

admin.site.register(Camp)
admin.site.register(Agency)
admin.site.register(Features)
admin.site.register(Photo)