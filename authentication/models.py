from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)

    
class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []
    username = None

