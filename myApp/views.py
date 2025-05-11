from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, "myApp/home.html")
class HomePageView(TemplateView):
    template_name = "myApp/home.html"

