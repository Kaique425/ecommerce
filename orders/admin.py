from orders.models import Orders
from django.contrib import admin
from orders.models import Orders, Item
from payments.models import PaymentModel

class PaymentInline(admin.TabularInline):
    model = PaymentModel
    can_delete = False
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
    ordering = ('-modified')
    
    def has_add_permission(self, request,obj):
        return False

class ItemInline(admin.TabularInline):
    extra = 0
    raw_id_fields = ['product']
    model = Item

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['__str__','cpf','name','email']
    list_filter = ['paid','cpf']
    inlines = [ItemInline]

