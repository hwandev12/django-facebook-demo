from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from post.models import FacebookPost
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

class PostAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = FacebookPost.objects.all()
    serializer_class = PostSerializer
    
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer