from payments.models import Payment
from django import forms


class PaymentForm(forms.ModelForm):
    token = forms.CharField()
    class Meta:
        model = Payment
        fields = [
            'transaction_amount',
            'installments',
            'payment_method_id',
            'doc_number',
            'email',
        ]
    
    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop('orders')
        super().__init__(*args, **kwargs)

    
    def transaction_amount_validation(self):
        transaction_amount = self.cleaned_data['transaction_amount']
        if float(transaction_amount) != float(self.order.get_total_price()):
            raise forms.ValidationError(
                'Transaction amount não condiz com o total da compra.'
            )
        return transaction_amount


    
