from rest_framework import serializers
from post.models import FacebookPost

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookPost
        fields = ('id', 'author', 'post_text', 'post_image', 'date_created', 'post_video')