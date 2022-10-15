from django import forms
from django.contrib.auth.forms import UserCreationForm
from requests import request
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


class Patientform(forms.ModelForm):

    name = forms.CharField()
    email = forms.EmailField(max_length=60, label='Email')
    phone = forms.CharField()
    
    class Meta:
        model = Patient
        fields = ('name', 'email', 'phone')

class Exerciseform(forms.ModelForm):

    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'h-20'}))
    video = forms.CharField()
    
    class Meta:
        model = Training
        fields = ('title', 'description', 'video')

class Courseform(forms.ModelForm):

    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    trainings = forms.ModelMultipleChoiceField(queryset=Training.objects.all(), widget=forms.CheckboxSelectMultiple)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'h-20'}))
    
    class Meta:
        model = Course
        fields = ('patient', 'trainings', 'description')