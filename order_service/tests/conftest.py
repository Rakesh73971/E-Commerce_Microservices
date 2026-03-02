import pytest
from orders.models import Order,OrderItem
from rest_framework.test import APIClient

@pytest.fixture
def order(db):
    return Order.objects.create(
        user_id = 1,
        total_price=100,
        status="PENDING"
        
    )

@pytest.fixture
def orderitem(order):
    return OrderItem.objects.create(
        order = order,
        product_id = 1,
        quantity = 1,
        price = 1000
    )

@pytest.fixture
def client(db): 
    return APIClient()