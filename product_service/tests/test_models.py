

def test_category_model(category):
    assert category.name == "bread"
    
def test_product_model(product):
    assert product.name == 'white bread'
    assert product.price == 200
