from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Budget(models.Model):
  #set them equal to the data field
  name = models.CharField(max_length=255)
  user = models.ForeignKey(User)
  description = models.TextField(blank=True)
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
  description = models.TextField(blank=True)
  maxAmount = models.DecimalField(decimal_places=2)

  def getTotalExpenses():
    expenseList = Entry.objects.filter()
    #pull all expenses from "any category" and add them up
    #see how pull from the tabel 
    #loop through them to add them up
    #querry the database and filter for the current field
    #go to expense table and bring back list
    #loop in this function to add
    totalExpenses = 

class Expense (models.Model):
  category = models.ForeignKey(Category)
  name = models.CharField(max_length=255)
  explanation = models.TextField(blank=True)
  amount = models.DecimalField(decimal_places=2)
