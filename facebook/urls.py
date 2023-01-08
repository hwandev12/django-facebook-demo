from django.urls import path, include
from .views import (
    post_list_view
)

app_name = 'facebook'

urlpatterns = [
    path('', post_list_view, name='home')
]
