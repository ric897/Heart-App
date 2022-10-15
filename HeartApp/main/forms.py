from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class Registration(UserCreationForm):
  email = forms.EmailField(max_length=60, label='Email', help_text='Required. Add a valid email address. Used to log in.')
  password1 = forms.CharField(label='Create password', widget=forms.PasswordInput())



  def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)

        for fieldname in ['email','password1', 'password2']:
            self.fields[fieldname].help_text = None

  class Meta: 
    model = NewUser
    fields = ['email', 'password1', 'password2']