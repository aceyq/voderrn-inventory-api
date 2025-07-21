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
    seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = "__all__"



