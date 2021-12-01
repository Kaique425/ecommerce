from django.urls import path
from .views import payment_create, SuccessView, PendingView, FailureView, payment_webhook

app_name = 'payment'

urlpatterns = [
    path('process/', payment_create, name='process_payment'),
    path('success/', SuccessView.as_view(), name='success' ),
    path('failure/', FailureView.as_view(), name='failure'),
    path('pending/', PendingView.as_view(), name='pending'),
    path('webhook/', payment_webhook, name='webhook')
]