from django.urls import path
from .views import PaymentCreate, SuccessView, PendingView, FailureView

app_name = 'payment'

urlpatterns = [
    path('process_payment', PaymentCreate.as_view(), name='create'),
    path('success', SuccessView.as_view(), name='success' ),
    path('failure', FailureView.as_view(), name='failure'),
    path('pending', PendingView.as_view(), name='pending'),
]