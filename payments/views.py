from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property
from orders.models import Orders
from django.views.generic import CreateView, TemplateView
from payments.models import Payment
from payments.forms import PaymentForm
from django.conf import settings



class SuccessView(TemplateView):
    template_name = 'payments/success.html'

class FailureView(TemplateView):
    template_name = 'payments/failure.html'

class PendingView(TemplateView):
    template_name = 'payments/pending.html'


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

    def form_valid(self, form):
        form.save()
        redirect_url = "payments:failure"
        status = form.instance.mercado_pago_status

        if status == "approved":
            redirect_url = "payments:success"
        if status == "in_process":
            redirect_url = "payments:pending"

        if status and status != "rejected":
            del self.request.session["order_id"]
        return redirect(redirect_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = self.order
        context["PUBLIC_KEY"] = settings.MERCADO_PAGO_PUBLIC_KEY
        return context

<<<<<<< HEAD
 
=======
    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
>>>>>>> Master
