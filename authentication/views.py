from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
            
        return super(CustomLoginView, self).form_valid(form)


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'account/signup.html'

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
    
# make classes functionable name
login_form_view = CustomLoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm)
register_form_view = RegisterView.as_view()