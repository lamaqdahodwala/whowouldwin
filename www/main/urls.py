from django.urls import path
from . import views

urlpatterns = [
    path('', views.Indexview.as_view(), name='index')
]