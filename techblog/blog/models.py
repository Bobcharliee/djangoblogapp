
from django.db import models


class blog(models.Model):
  author = models.CharField(max_length=40)
  title= models.CharField(max_length=40)
  description= models.TextField()
  
  def __str__(self):
    return self.title