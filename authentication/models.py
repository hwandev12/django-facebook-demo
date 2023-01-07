from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, gender, password=None, **other_fields):

        if not email:
            raise ValueError("Please, user should provide email address!")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, gender, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, gender, password=None, **other_fields):

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


GENDER = (('man', 'Man'), ('woman', 'Woman'))


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=250,
        unique=True,
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        # yes all admins
        return self.is_admin

class Profile(models.Model):
    """
    To create profile page, we need to create class related to OneToOneField with
    CustomUser
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    avatar = models.ImageField(default='default.jpg', upload_to='profile')

    def __str__(self):
        return self.user.email