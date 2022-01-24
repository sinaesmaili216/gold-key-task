from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CreditCharge(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.customer} --> {self.price}'


