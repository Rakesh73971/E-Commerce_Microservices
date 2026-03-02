

def test_order_model(order):
    assert order.total_price == 100
    assert order.status == 'PENDING'

def test_orderitem_model(orderitem):
    assert orderitem.quantity == 1
    assert orderitem.price == 1000