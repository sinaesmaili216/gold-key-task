import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from basket.models import Order, Basket, OrderItem
from content.models import Content
from customer.models import Customer, CreditCharge


@login_required(login_url='/customer/login/')
def basket(request):
    try:
        # all content items that user saved to his basket
        order_items = OrderItem.objects.filter(order__customer__user=request.user)
        order = Order.objects.get(customer__user=request.user)
    except Order.DoesNotExist:
        order = None
    finally:
        # get user's credit charge if available to apply discount
        try:
            credit_charge = CreditCharge.objects.get(customer__user=request.user)
        except CreditCharge.DoesNotExist:
            credit_charge = None
    return render(request, 'basket/basket-contents.html', context={'order_items': order_items, 'order': order, 'credit_charge': credit_charge})


@login_required(login_url='/customer/login/')
def add_to_basket(request):
    data = json.loads(request.body)
    contentId = data['contentId']

    # print(action, productId)
    customer = Customer.objects.get(user=request.user)

    content = Content.objects.get(id=contentId)
    order, created = Order.objects.get_or_create(customer=customer)
    basket, created = Basket.objects.get_or_create(customer=customer)
    order_item = OrderItem.objects.get_or_create(order=order, content=content, basket=basket)

    return JsonResponse('item added', safe=False)
