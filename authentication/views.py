from django.shortcuts import redirect, render
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

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
            form.save(commit=False)
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {first_name}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

@login_required
def profile_section_view(request):
    return render(request, 'account/profile.html')


# make classes functionable name
login_form_view = CustomLoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm)
register_form_view = RegisterView.as_view()