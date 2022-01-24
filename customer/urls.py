from django.urls import path

from customer.views import login_user, logout_user, register_user

app_name = 'customer'
urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]
