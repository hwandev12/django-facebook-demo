from django.shortcuts import redirect, render, get_object_or_404
from django.urls import resolve, reverse
from .forms import UserCreationForm, LoginForm, UpdateUserForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.utils.timezone import now
import pytz
from datetime import datetime, timedelta
from pytz import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            # Update last visit time after request finished processing.
            User.objects.filter(pk=request.user.pk).update(last_login=now())
        return response


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        user = form.cleaned_data.get("username")
        messages.success(self.request, "Welcome " + user)
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)


class RegisterView(View):
    form_class = UserCreationForm
    initial = {'key': 'value'}
    template_name = 'account/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


@login_required
def profile_section_view(request, user_name):
    user_n = User.objects.get(username=user_name)
    current_user = request.user

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        'user_n': user_n,
    }
    return render(request, 'account/profile.html', context)

# make classes functionable name
login_form_view = CustomLoginView.as_view(
    redirect_authenticated_user=True, authentication_form=LoginForm)
register_form_view = RegisterView.as_view()
