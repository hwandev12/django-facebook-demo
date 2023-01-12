from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import get_user_model

from .models import CustomUser, Profile

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """
    This is for creating new user that is coming from custom model
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'gender', 'username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password didn't match!")
        return password2

    def save(self, commit=True):
        """
        Save user with hashed password
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ For updating users """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username', 'gender', 'is_active', 'is_admin')


# login form
class LoginForm(AuthenticationForm):
    password = forms.CharField(max_length=50, required=True)
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'remember_me']

GENDER = (('man', 'Man'), ('woman', 'Woman'))

class UpdateUserForm(forms.ModelForm):
    """
    UpdateUserForm interacts with the user model to let users 
    update their username and email.
    """
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'gender']
        
class UpdateProfileForm(forms.ModelForm):
    """
    UpdateProfileForm interacts with the profile model
    to let users update their profile.
    """
    avatar = forms.ImageField()
    bio = forms.CharField(max_length=300)
    
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
    