from django.urls import path
from . import views

urlpatterns = [
    path('', views.Indexview.as_view(), name='index'),
    path('newfight', views.new_fight, name='newfight')
]