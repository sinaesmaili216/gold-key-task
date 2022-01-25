from django.db import models

from content.models import Content
from customer.models import Customer, CreditCharge


class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    PAYMENT_STATUS_PENDING = 'در انتظار'
    PAYMENT_STATUS_COMPLETE = 'تایید شده'

    PAYMENT_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'در انتظار'),
        (PAYMENT_STATUS_COMPLETE, 'تایید شده')
    ]
    payment_status = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default=PAYMENT_STATUS_PENDING)

    def __str__(self):
        return f'{self.customer} : {self.payment_status}'

    def total_price(self):
        items = OrderItem.objects.filter(order__customer=self.customer)
        prices = [item.content.price for item in items if isinstance(item.content.price, int)]
        try:
            credit_charge = CreditCharge.objects.get(customer=self.customer).price
            return sum(prices) - credit_charge
        except CreditCharge.DoesNotExist:
            return sum(prices)


class OrderItem(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    basket = models.ForeignKey(Basket, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content.title
