from orders.models import Orders
from django.contrib import admin
from orders.models import Orders, Item

class ItemInline(admin.TabularInline):
    extra = 0
    raw_id_fields = ['product']
    model = Item

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['__str__','cpf','name','email']
    list_filter = ['paid','cpf']
    inlines = [ItemInline]

