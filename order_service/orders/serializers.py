from rest_framework import serializers
from .models import OrderItem,Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user_id','total_price','status','created_at','updated_at']

class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order')
    class Meta:
        model = OrderItem
        fields = ['id','order','order_id','product_id','quantity','price']