from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from post.models import FacebookPost
    
class PostListView(ListView):
    model = FacebookPost
    context_object_name = 'posts'
    template_name = 'pages/home.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# make class names to function names
post_list_view = PostListView.as_view()

