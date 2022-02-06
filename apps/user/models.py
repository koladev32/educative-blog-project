from django.db import models
from django.contrib.auth.models import (BaseUserManager, PermissionsMixin, AbstractBaseUser)
from apps.abstract.models import AbstractModel, AbstractManager


class UserManager(BaseUserManager, AbstractManager):

    def create_user(self, username, first_name, last_name, password, email, **extra_fields):

        if email is None:
            raise TypeError("User must have a phone phone")

        if first_name is None:
            raise TypeError("User must have a first name")

        if last_name is None:
            raise TypeError("User must have a last name")

        if password is None:
            raise TypeError("You should put a password")

        if username is None:
            raise TypeError("You should put a username")

        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, password, email, **extra_fields):

        user = self.create_user(username, first_name, last_name, password, email, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractModel, PermissionsMixin, AbstractBaseUser):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=35, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name