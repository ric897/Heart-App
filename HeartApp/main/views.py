
from django.shortcuts import redirect, render
from django.template import base
from twilio.rest import Client
from .serializers import *
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
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from rest_framework.viewsets import ModelViewSet

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
        return super(Resourceform, self).form_valid(form)

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

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UserViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer

class TrainingViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    
class ResourcesViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class NestedViewSet(ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NestedSerializer