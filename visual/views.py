from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .forms import ApplicationDetailForm
from .models import Producer, CreditApplication


class AddBookView(FormView):
    template_name = 'home.html'
    form_class = ApplicationDetailForm

    def get_success_url(self):
        application_id = self.request.POST.get('application_id', None)
        if application_id:
            return str(application_id)
        else:
            reverse('home')


class ApplicationProducersDetailView(ListView):
    model = Producer
    template_name = 'application_producer_details.html'
    context_object_name = 'producers'

    def get_queryset(self):
        apl_id = self.kwargs.get('apl_id')
        try:
            postions = CreditApplication.objects.get(pk=apl_id).related_contract.position_set.all()
        except ObjectDoesNotExist:
            return None

        producers = set()
        for postion in postions:
            producers.add(postion.related_producer)

        return producers
