from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    

# make class names to function names
home_page_view = HomePageView.as_view()

