from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class InnovationLionView(TemplateView):
    template_name = 'description/lion_description.html'


class InnovationTigerView(TemplateView):
    template_name = 'description/tiger_description.html'