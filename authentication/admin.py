from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from .models import (
    CustomUser
)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_superuser')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)