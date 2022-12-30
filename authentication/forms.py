from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm    


class RegisterForm(SignupForm):
    first_name = forms.CharField(max_length=100, label='First Name')
    surname = forms.CharField(max_length=100, label='Surname')

    def save(self, request):
        user = super(RegisterForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.surname = self.cleaned_data['surname']
        user.save()
        return user
    
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )
        
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )
        

    
