from django.shortcuts import render
from .models import Ingredient, Receipe
from rest_framework import viewsets, permissions
from .serializers import IngredientSerializer, ReceipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited
    """
    queryset = Ingredient.objects.all().order_by('-name')
    serializer_class = IngredientSerializer
    permission_classes = [permissions.AllowAny]


class ReceipeViewSet(viewsets.ModelViewSet):
    queryset = Receipe.objects.all().order_by('-pub_date')
    serializer_class = ReceipeSerializer
    permission_classes = [permissions.AllowAny]
