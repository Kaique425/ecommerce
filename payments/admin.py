from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'transaction_amount',
        'installments',
        'payment_method_id',
        'email',
        'doc_number',
        'mercado_pago_id',
        'mercado_pago_status',
        'mercado_pago_status_detail',
        'created',
        'modified'
    ]
    list_filter = ['mercado_pago_status','modified']