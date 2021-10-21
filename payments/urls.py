from django.urls import path
from .views import PaymentCreate

app_name = 'payment'

urlpatterns = [
    path('create', PaymentCreate.as_view(), name='create')
]