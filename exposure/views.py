from .models import Incident
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import IncidentSerializer

# Create your views here.

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.AllowAny]