from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView

from App.models import Man


class HelloView(View):
    def get(self,request):
        return HttpResponse('GET OK')

    def post(self,request):
        return HttpResponse('POST OK')
class TemplateView(TemplateView):
    pass

class HelloListView(ListView):

    template_name = "mans.html"

    queryset = Man.objects.all()