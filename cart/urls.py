from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path('',views.cart, name='detail'),
    path('add/<str:id>',views.product_add, name='add'),
]