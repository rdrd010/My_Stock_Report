from django.shortcuts import render

from django.views import generic
from django.views import View

class Stock_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'stock_main/index.html'
        return render(request, template_name)
