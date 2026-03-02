import pytest
from products.models import Category,Product
from rest_framework.test import APIClient


@pytest.fixture
def client(db):
    return APIClient()

@pytest.fixture
def category(db):
    return Category.objects.create(
        name="bread"
    )

@pytest.fixture
def product(category):
    return Product.objects.create(
        name="white bread",
        price=200,
        category=category
    )