from rest_framework import serializers
from products.models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','category','category_name','created_at','updated_at']
