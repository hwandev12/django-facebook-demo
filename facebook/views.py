from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from post.forms import PostForm
from django.views import View
import datetime
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
from django.utils import timezone

from post.models import FacebookPost

class PostCreateByUserListView(CreateView):
    form_class = PostForm
    template_name = 'pages/home.html'
    context_object_name = 'form'

    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('facebook:home')

    def get_context_data(self, **kwargs):
        kwargs['posts'] = FacebookPost.objects.all()
        return super(PostCreateByUserListView, self).get_context_data(**kwargs)

# make class names to function names
post_list_view = PostCreateByUserListView.as_view()

