from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self,email,password,is_staff=False, is_active=False,**extra_fields):
        e=extra_fields.pop('email', None)
        user=self.model(
            email=email,
            is_active=is_active,
            is_staff=is_staff,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user
class create_superuser(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        e=extra_fields.pop('email', None)
        user=self.model(
            email=email,
            is_active=True,
            is_staff=True,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=12, null=True, blank=True,unique=True)
    fullname=models.CharField(max_length=300, null=True, blank=True)
    phone=models.CharField(max_length=30,blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True, blank=True)
    USERNAME_FIELD = ''