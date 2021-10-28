from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from orders.models import Orders
from django.views.generic import CreateView
from payments.models import Payment
from payments.forms import PaymentForm
from django.conf import settings


class PaymentCreate(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/create.html'

    @cached_property
    def order(self):
        order_id = self.request.session.get("order_id")
        order = get_object_or_404(Orders, id=order_id)
        return order

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["order"] = self.order
        return form_kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PUBLIC_KEY'] = settings.MERCADO_PAGO_PUBLIC_KEY
        return context

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)