from django.db import models

# Create your models here.
class Family(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(default='')
  age = models.IntegerField()
  address = models.TextField(null=True, blank=True)

class Cars(models.Model):
  name = models.CharField(max_length=100,default='')
  speed = models.IntegerField(default=50)
  
  def __str__(self):
    return self.name