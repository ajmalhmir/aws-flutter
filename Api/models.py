from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
   

