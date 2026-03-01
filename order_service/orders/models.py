from django.db import models

# Create your models here.

class Order(models.Model):

    STATUS_CHOICE=(
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('SHIPPED','Shipped'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled')
    )
    user_id = models.IntegerField()

    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='PENDING')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"Item {self.product_id} in Order {self.order.id}"
    