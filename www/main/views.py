from django.shortcuts import render
from django.views.generic import ListView
from .models import Fight

# Create your views here.
class Indexview(ListView):
    model = Fight
    template_name = 'main/index.html'