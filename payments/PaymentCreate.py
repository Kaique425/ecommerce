from .models import PaymentModel

def payment_create_model(request, payment_response, order):
    
    if payment_response['status'] == 201:
        Payment = PaymentModel.objects.create(
            order = order,
            transaction_amount = float(order.get_total_price()),
            installments = int(request.POST.get("installments")),
            payment_method_id = request.POST.get("paymentMethodId"),
            email = request.POST.get("email"),
            doc_number = request.POST.get("docNumber"),
            mercado_pago_id = payment_response['response']['id'] ,
            mercado_pago_status = payment_response['response']['status'],
            mercado_pago_status_detail = payment_response['response']['status_detail'],
            )
        if payment_response['response']['status'] == 'approved':
            order.paid = True
            order.save()
            
    return Payment.save()