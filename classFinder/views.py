from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClassSectionsSerializer
from .models import ClassSections

# Create your views here.

class ClassSectionsView(viewsets.ModelViewSet):
    serializer_class = ClassSectionsSerializer
    queryset = ClassSections.objects.all()