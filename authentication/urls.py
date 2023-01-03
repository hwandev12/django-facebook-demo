from django.urls import path, include
from .views import (
    register_form_view,
    login_form_view
)
from django.contrib.auth.views import LogoutView as logout_form_view
from django.contrib.auth.views import LoginView

app_name='authenticate'

urlpatterns = [
    path('register/', register_form_view, name='user-register'),
    path('login/', login_form_view, name='user-login'),
    path('logout/', logout_form_view.as_view(), name='user-logout'),
]