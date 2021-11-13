from django.urls import path
from . import views

app_name = 'cartapp'

urlpatterns = [
        path('', views.index, name='index'),
        path('register', views.register_process, name='register'),
        path('login', views.login_process, name='login'),
        path('logout', views.logout_process, name='logout'),
        path('cart', views.cart, name='cart'),
        path('checkout', views.checkout, name='checkout'),
]
