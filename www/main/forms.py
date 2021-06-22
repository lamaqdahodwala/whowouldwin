from django.forms import ModelForm
from .models import Fight

class FightForm(ModelForm):
    class Meta:
        model = Fight
        fields = ['red', 'blue']