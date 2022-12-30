from django.contrib import admin
from .models import MyCustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyCustomUser
    list_display = ['email', 'username', 'is_superuser']

admin.site.register(MyCustomUser, CustomUserAdmin)