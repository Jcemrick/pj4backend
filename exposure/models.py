from django.db import models

# Create your models here.
class Incident(models.Model):
    incidentid = models.IntegerField(blank=True, null=True)
    responsetype = models.CharField(max_length=100)
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    enddate = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=150)
