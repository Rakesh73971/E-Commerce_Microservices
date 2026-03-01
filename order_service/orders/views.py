from rest_framework import viewsets
from .serializers import OrderSerializer,OrderItemSerializer
from .models import Order,OrderItem
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related('order').all()
    serializer_class = OrderItemSerializer