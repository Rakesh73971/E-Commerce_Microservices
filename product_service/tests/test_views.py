from products.models import Category,Product


def test_create_category(client):
    response = client.post(
        "/products/categories/",
        {
            "name":"bread"
        },
        format="json"
    )
    assert response.status_code == 201
    assert Category.objects.count() == 1

def test_create_product(client,category):
    response = client.post(
        "/products/products/",
        {
            "name":"white bread",
            "price":200,
            "category":category.id
        },
        format="json"
    )
    assert response.status_code == 201
    assert response.data["name"] == "white bread"
    assert Product.objects.count() == 1