from orders.models import Order,OrderItem


def test_create_order(client):
    response = client.post(
        "/orders/orders/",
        {
            "user_id":1,
            "total_price":100,
            "status":"PENDING"
        },
        format="json"
    )
    assert response.status_code == 201
    assert Order.objects.count() == 1

def test_create_orderitems(client, order):
    response = client.post(
        '/orders/orderitems/',
        {
            "order": order.id,   
            "product_id": 1,
            "quantity": 1,
            "price": 2000
        },
        format="json"
    )

    assert response.status_code == 201
    assert OrderItem.objects.count() == 1