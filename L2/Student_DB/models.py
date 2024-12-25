from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField(null=True, blank=True)
  email = models.EmailField()
  address = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
  name = models.CharField(max_length=100 , default="Unnamed Product")
  price = models.FloatField(default=0.0)