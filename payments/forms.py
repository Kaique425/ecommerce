from payments.models import Payment
from django.conf import settings
from django import forms
import mercadopago


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
    
    #def __init__(self, *args, **kwargs):
        #self.order = kwargs.pop('orders')
        #super().__init__(*args, **kwargs)

    
    def transaction_amount_validation(self):
        transaction_amount = self.cleaned_data['transaction_amount']
        if float(transaction_amount) != float(self.order.get_total_price()):
            raise forms.ValidationError(
                'Transaction amount não condiz com o total da compra.'
            )
        return transaction_amount


    def save(self):
        cd = self.cleaned_data 
        mp = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
        payment_data = {
            "transaction_amount" : float(self.order.get_total_price()),
            "token" : cd["token"],
            "description" : self.order.get_description(),
            "installments" : cd['installments'],
            "payment_method_id" : cd["payment_method_id"],
            "payer" : {
                "email" : cd["email"],
                "identification" : {"type" : "cpf", "number" : cd["doc_number"]}
            }
        }

        payment =  mp.payment().create(payment_data)

        if payment["status"] == 201:
            self.instance.order = self.order
            self.instance.mercado_pago_id = payment["response"]["id"]
            self.instance.mercado_pago_status_detail = payment["response"]["status_detail"]
            self.instance.mercado_pago_status = payment["response"]["status"]

            if payment["response"]["status"] == "approved":
                self.order.paid = True
                self.order.save()
            self.instance.save()
        