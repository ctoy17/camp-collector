from django.forms import ModelForm
from .models import Agency

class AgencyForm(ModelForm):
    class Meta:
        model = Agency
        fields = ['organization']

