from django.contrib import admin
from .models import PaymentModel

@admin.register(PaymentModel)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'order',
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
    readonly_fields = (
         "email",
        "doc_number",
        "transaction_amount",
        "installments",
        "payment_method_id",
        "mercado_pago_id",
        "mercado_pago_status",
        "mercado_pago_status_detail",
        "modified",   
    )