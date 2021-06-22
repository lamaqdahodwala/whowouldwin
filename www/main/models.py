from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fight(models.Model):
    red = models.CharField(max_length=50)
    blue = models.CharField(max_length=50)
    op = models.ForeignKey(User, on_delete=models.CASCADE)