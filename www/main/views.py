from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def index(req):
    return render(req, 'main/index.html')