from django.urls import path
from . import views

urlpatterns = [
    path('', views.Indexview.as_view(), name='index'),
    path('newfight', views.new_fight, name='newfight'),
    path('fight/<int:pk>', views.view_fight, name='view_fight'),
    path("fight/vote/blue/<int:pk>", views.blue_vote, name='bluevote'),
    path('fight/vote/red/<int:pk>', views.red_vote, name='red_vote')
]