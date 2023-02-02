from rest_framework import serializers
from post.models import FacebookPost
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookPost
        fields = ('id', 'author', 'post_text', 'post_image', 'date_created', 'post_video')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ("id", "username")