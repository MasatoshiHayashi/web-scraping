from django.db import models

class Dating(models.Model):
    month = models.CharField(max_length=2)
    spot = models.CharField(max_length=100)
# Create your models here.
