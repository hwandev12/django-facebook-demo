from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from .models import (
    CustomUser
)


admin.site.register(CustomUser)
admin.site.unregister(Group)