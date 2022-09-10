from django.db import models
from  .Customer import User
from .Product import Picture
import datetime

class Order(models.Model):
    product = models.ForeignKey(Picture, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

    def __str__(self):
        return self.product.name
    

    @staticmethod
    def getOrderByCustomer(customer_id):
        return Order.objects.filter(customer = customer_id)