from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path('',views.cart, name='detail'),
    path('add/<str:id>/',views.add_product, name='add'),
    path('remove/<str:id>/', views.remove_product, name='remove'),
]