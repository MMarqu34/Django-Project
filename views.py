from django.shortcuts import render 
from rest_framework import viewsets
from .models import user_reg
from .serializers import user_regSerializer


class user_regView(viewsets.ModelViewSet):
    queryset = user_reg.objects.all()
    serializer_class = user_regSerializer
