from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=55)
    city=models.CharField(max_length=12)
    age=models.IntegerField()