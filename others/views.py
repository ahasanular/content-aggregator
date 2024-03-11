from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm


class AboutUsView(TemplateView):
    template_name = 'about.html'


class ContactUsView(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_us_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactUsSuccessView(TemplateView):
    template_name = 'contact_us_success.html'