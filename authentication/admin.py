from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Profile
from .forms import (
    UserChangeForm,
    UserCreationForm
)
from .models import (
    CustomUser,
    Profile,
)
    
class ProfileInline(admin.TabularInline):
    model = Profile

class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    inlines = [
        ProfileInline,
    ]
    
    list_display = ('email', 'username', 'is_active', 'is_admin', 'is_staff',)
    list_filter = ('is_admin',)
    fieldsets = (
        ('Changeable points', {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender',)}),
        ('Permissions', {'fields': ('is_admin', 'user_permissions', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)