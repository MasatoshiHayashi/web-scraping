from django.db import models

class News(models.Model):
    url = models.CharField(max_length=1000)
# Create your models here.
