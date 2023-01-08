from django import forms
from .models import FacebookPost

class PostForm(forms.ModelForm):
    """
    that can create post that would bind to template, user can create
    post via html template using model objects
    """
    
    class Meta:
        model = FacebookPost
        fields = ('post_text', 'post_image',)
    