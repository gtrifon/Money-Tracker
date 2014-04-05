from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Budget(models.Model):
  #set them equal to the data field
  name = models.CharField(max_length=255)
  user = models.ForeignKey(User)
  ##optional##
  description = models.TextField()
  purpose = models.CharField(max_length=255)

class Category (models.Model):
  JANUARY = 1
  FEBRUARY = 2
  MARCH = 3
  APRIL = 4
  MAY = 5
  JUNE = 6
  JULY = 7
  AUGUST = 8
  SEPTEMBER = 9
  OCTOBER = 10
  NOVEMBER = 11
  DECEMBER = 12

  MONTH_CHOICES = ((JANUARY, 'January'),
    (FEBRUARY, 'February'),
    (MARCH, 'March'),
    (APRIL, 'April'),
    (MAY, 'May'),
    (JUNE, 'June'),
    (JULY, 'July'),
    (AUGUST, 'August'),
    (SEPTEMBER, 'September'),
    (OCTOBER, 'October'),
    (NOVEMBER, 'November'),
    (DECEMBER, 'December'),
  )

  budget = models.ForeignKey(Budget)
  name = models.CharField(max_length=255)
  month = models.IntegerField(choices=MONTH_CHOICES)
  year = models.IntegerField()
  ##optional##
  description = models.TextField(blank=True)
  maxAmount = models.DecimalField(decimal_places=2)

class Expense (models.Model):
  category = models.ForeignKey(Category)
  explanation = models.TextField()
  amount = models.DecimalField(decimal_places=2)
