from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'
    login_url = 'account_login'
    

# make class names to function names
home_page_view = HomePageView.as_view()

