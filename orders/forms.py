from django import forms
from django import forms
from orders.models import Orders


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = [
            'name', 
            'cpf', 
            'email', 
            'postal_code', 
            'address', 
            'number',
            'district', 
            'state',
            'city',
            'compliment',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postal_code'].widget.attrs.update({'onchange': 'getAddress()'})