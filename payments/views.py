import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.functional import cached_property
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Orders, PaymentModel
from django.views.generic import TemplateView
from payments.models import PaymentModel
from django.conf import settings
from .PaymentCreate import payment_create_model
import mercadopago

class SuccessView(TemplateView):
    template_name = 'payments/success.html'

class FailureView(TemplateView):
    template_name = 'payments/failure.html'

class PendingView(TemplateView):
    template_name = 'payments/pending.html'



def payment_create(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Orders, id=order_id)
    context = {
        'PUBLIC_KEY': settings.MERCADO_PAGO_PUBLIC_KEY, 
        'order' : order
    }
    
    if request.method == 'POST':
        sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
        payment_data = {
            "transaction_amount": float(request.POST.get("transactionAmount")),
            "token": request.POST.get("token"),
            "description": request.POST.get("description"),
            "installments": int(request.POST.get("installments")),
            "payment_method_id": request.POST.get("payment_method_id"),
            "payer": {
                "email": request.POST.get("email"),
                "identification": {
                    "type": request.POST.get("type"), 
                    "number": request.POST.get("number")
                }
            }
        }

        payment_response = sdk.payment().create(payment_data)
        status = payment_response['response']['status']
    
        redirect_url = 'payment:failure'
        
        if status == 'approved':
            redirect_url = 'payment:success'
        if status == 'in_process':
            redirect_url = 'payment:pending'
        
        if status and status != 'rejected':
            del request.session['order_id']
            
        payment_create_model(request, payment_response, order)
        return redirect(redirect_url)

    return render(request,'payments/create.html', context)


@csrf_exempt
@require_POST
def payment_webhook(request):
    data = json.loads(request.body)
    mp = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)
    
    if data['action'] == "approved":
        mp_id = data['data']['id']
        payment_mp = mp.payment.get(mp_id)
        payment = PaymentModel.objects.get(mercado_pago_id=mp_id)
        
        payment.mercado_pago_status = payment_mp['response']['status']
        payment.mercado_pago_status_detail = payment_mp['response']['status_detail']
        
        if payment_mp['response']['status'] == 'approved':
            payment.order.paid = True
        else:
            payment.order.paid = False
        
        payment.order.save()
        payment.save()
    
    return JsonResponse({})