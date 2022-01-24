from django.urls import path
from basket.views import basket, add_to_basket

app_name = 'basket'
urlpatterns = [
    path('basket/', basket, name='basket'),
    path('add_to_basket/', add_to_basket, name='add_to_basket')
]
