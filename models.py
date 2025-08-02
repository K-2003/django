from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.TextField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    order_type = models.CharField(max_length=20)
    delivery_time = models.CharField(max_length=50)

    def __str__(self):
        return f'Order #{self.id} by {self.user.username}'
