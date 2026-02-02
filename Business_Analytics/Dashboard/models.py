from django.db import models

# Create your models here.
class BusinessRecord(models.Model):
    category = models.CharField(max_length=100)
    value = models.FloatField()
    date = models.DateField()

    