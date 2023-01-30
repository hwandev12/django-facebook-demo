from django.shortcuts import render
from rest_framework import generics, permissions

from post.models import FacebookPost
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostAPIView(generics.ListCreateAPIView):
    queryset = FacebookPost.objects.all()
    serializer_class = PostSerializer
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated)
    queryset = FacebookPost.objects.all()
    serializer_class = PostSerializer