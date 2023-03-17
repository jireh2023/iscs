from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects=models.Manager()

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def __str__(self):
        return "Username: {}, Password: {}".format(self.username, self.password)

class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name

    def getDesc(self):
        return self.description
    
    def getPrice(self):
        return self.price

    def __str__(self):
        return "{}: {} - {}, {}".format(self.pk, self.name, self.price, self.description)

class Customer(models.Model):
    customername = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def getName(self):
        return self.customername

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def __str__(self):
        return "{}: {} - {}, {}".format(self.pk, self.customername, self.address, self.city)

class Order(models.Model):
    payment_mode_choices = [
        ("Cash", "Cash"),
        ("Card", "Card"),
    ]

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.FloatField(max_length=50)
    ordered_at = models.DateTimeField(blank=True, null=True)
    cust_order = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=50, choices=payment_mode_choices, default='Cash')

    def getMode(self):
        return self.payment_mode

    def getQuantity(self):
        return self.qty
    
    def __str__(self):
        return "Order {}: {} ({}). For {}. Mode of payment: {}, ordered at {}".format(self.pk, self.food.getName(), self.qty, self.cust_order.getName(), self.payment_mode, self.ordered_at)