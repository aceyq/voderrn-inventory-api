#serializer takes Python objects and turns them into JSON
#JSON - standard format that APIs use to send/receive data

from rest_framework import serializers
from .models import User, Category, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    #fields means include EVERY filed in the model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta: #doesn't inherit from anything, just holds config settings
        model = Product
        fields = "__all__"


