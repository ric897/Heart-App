
from django.shortcuts import redirect, render
from django.template import base
from twilio.rest import Client
from .forms import *
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    return render(request, 'index.html', context)

@login_required
def dashboard(request):
    context = {}
    context['patients'] = Patient.objects.filter(supervisor = request.user)
    context['exercises'] = Training.objects.all()
    context['resources'] = Resource.objects.all()
    endpoint = "https://api.assemblyai.com/v2/transcript/rk5e8ry4z7-78fd-475d-86d8-0f2ba358d91b"
    headers = {
        "authorization": "e72231891f984135a0e02e75d0265e09",
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    return render(request, 'dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class RegisterPage(FormView):
    redirect_authenticated_user = True
    template_name = 'register.html'
    form_class = Registration

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')

class PatientCreate(LoginRequiredMixin, CreateView):
    form_class = Patientform
    template_name = 'patientcreate.html'

    def form_valid(self, form):
        form.instance.supervisor = self.request.user
        return super(PatientCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')

class ExerciseCreate(LoginRequiredMixin, CreateView):
    form_class = Exerciseform
    template_name = 'exercisecreate.html'

    def form_valid(self, form):
        return super(ExerciseCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class ResourceCreate(LoginRequiredMixin, CreateView):
    form_class = Resourceform
    template_name = 'resourcecreate.html'

    def form_valid(self, form):
        return super(ResourceCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')

class CourseCreate(LoginRequiredMixin, CreateView):
    form_class = Courseform
    template_name = 'coursecreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super(CourseCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')


class CourseDetail(DetailView):
    model = Course
    template_name = 'coursedetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AudioCreate(LoginRequiredMixin, CreateView):
    form_class = Audioform
    template_name = 'audioform.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.supervisor = self.request.user
        return super(AudioCreate, self).form_valid(form)