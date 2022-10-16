import email
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import socket

from matplotlib.pyplot import title
socket.gethostbyname("")
from django.template.loader import render_to_string
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator 




class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    goal = models.CharField(max_length=150, blank=True)
    promo = models.BooleanField(default=True)
    terms = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name',]

    def __str__(self):
        return self.email


class Patient(models.Model):
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Training(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Resource(models.Model):
    title = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.link


class Course(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    trainings = models.ForeignKey(Training, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
