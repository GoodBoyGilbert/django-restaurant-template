from django.db import models

# Create your models here.

class Menu(models.Model):
  img = models.ImageField(upload_to="media")
  name = models.CharField(max_length=30)
  desc = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=30)

class Lunch(models.Model):
  img = models.ImageField("media")
  name = models.CharField(max_length=30)
  desc = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=30)

class Dinner(models.Model):
  img = models.ImageField("media")
  name = models.CharField(max_length=30)
  desc = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=30)