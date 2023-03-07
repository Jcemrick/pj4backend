from .models import Incident
from rest_framework import serializers

class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incident
        fields = [
            'id', 
            'incidentid', 
            'responsetype',
            'smokepresent',
            'smokecolor',
            'startdate', 
            'time', 
            'exposuretime', 
            'address' 
            ]