from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AdminSerializer
from .models import Admin
# Create your views here.

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class =AdminSerializer