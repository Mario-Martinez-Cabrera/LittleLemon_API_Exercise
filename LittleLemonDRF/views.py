from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rating
from .serializers import RatingSerializer
from rest_framework.viewsets import ModelViewSet

class RatingsView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

#class RatingsView(generics.ListCreateAPIView):
#    queryset = Rating.objects.all()
#    serializer_class = RatingSerializer

def get_permissions(self):
    if(self.request.method=='GET'):
        return []

    return [IsAuthenticated()]


