from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone', 'link']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        fields = "__all__"

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.SerializerMethodField
    class Meta:
        model = Resource
        fields = "__all__"

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.SerializerMethodField
    trainings = serializers.SerializerMethodField
    class Meta:
        model = Course
        fields = "__all__"