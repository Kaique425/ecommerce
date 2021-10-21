from django.views.generic import CreateView
from payments.models import Payment
from payments.forms import PaymentForm
from django.conf import settings


class PaymentCreate(CreateView):
    form_class = PaymentForm
    template_name = 'payments/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PUBLIC_KEY'] = settings.MERCADO_PAGO_PUBLIC_KEY
        return context

