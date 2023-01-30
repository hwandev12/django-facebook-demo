from django.urls import path
from .views import PostAPIView, PostDetailView

urlpatterns = [
    path('', PostAPIView.as_view()),
    path('<uuid:pk>/', PostDetailView.as_view()),
]