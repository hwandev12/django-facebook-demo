from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


GENDER = (('man', 'Man'), ('woman', 'Woman'))

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=50, required=True)
    password2 = forms.CharField(max_length=50, required=True)
    gender = forms.ChoiceField(choices=GENDER)

    class Meta:
        model = User
        fields = ['first_name', 'surname', 'email', 'password1', 'password2']

# login form
class LoginForm(AuthenticationForm):
    """Authenticate user in django by customizable"""
    username = forms.EmailField(required=True)
    password = forms.CharField(max_length=50)
    remember_me = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']