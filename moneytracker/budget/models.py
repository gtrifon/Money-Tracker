from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Budget(models.Model):
  #set them equal to the data field
  name = models.CharField(max_length=255)
  user = models.ForeignKey(User)
  description = models.TextField()
  purpose = models.CharField(max_length=255)
