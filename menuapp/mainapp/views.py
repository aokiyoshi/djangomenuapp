from django.shortcuts import render
from django.views.generic import TemplateView

from .models import MenuItem


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['navbar'] = [{'title': item.title, 'address': item.address,
                              'parent': (item.parent if item.parent else '')} for item in MenuItem.objects.all()]

        print(context['navbar'])
        return context
