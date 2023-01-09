from django.shortcuts import redirect, render, get_object_or_404
from django.urls import resolve
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

User = get_user_model()


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
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


@login_required
def profile_section_view(request, pk):
    user_n = get_object_or_404(User, id=pk)
    current_user = request.user
    toast_user = False

    if current_user.has_perm('authentication.special_status_edit'):
        user_n = get_object_or_404(User, id=pk)
        toast_user = True
    elif not current_user.has_perm('authentication.special_status_other'):
        user_n = get_object_or_404(User, id=pk)
        toast_user = False

    content_type = ContentType.objects.get_for_model(Profile)
    permission = Permission.objects.get(
        codename='special_status_edit',
        content_type=content_type,
    )
    user_n.user_permissions.add(permission)

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
        'toast_user': toast_user
    }
    return render(request, 'account/profile.html', context)


# make classes functionable name
login_form_view = CustomLoginView.as_view(
    redirect_authenticated_user=True, authentication_form=LoginForm)
register_form_view = RegisterView.as_view()

# ertagalik ishimda katta qilib har bitta user uchun bittadan permission beriladi ular shunchaki ko'rinishi uchun
# lekin request.user uchun ikkita permission yaratiladi, 1-o'zini profilini ko'rish, 2-boshqalarni profileni prosta ko'rishga 
