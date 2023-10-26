from .models import Ingredient, Receipe
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'type_ingr', 'nutriscore', 'season', 'image']


class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = ['name', 'pub_date', 'ingredients', 'type_receipe', 'theme', 'source', 'time', 'difficulty', 'regimes', 'image', 'description']
