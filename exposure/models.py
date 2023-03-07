from django.db import models

# Create your models here.
class Incident(models.Model):
    incidentid = models.IntegerField(blank=True, null=True)
    responsetype = models.CharField(max_length=100)
    smokepresent = models.BooleanField(null=True, default=True)
    smokecolor = models.CharField(max_length=100)
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    exposuretime = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=150)
