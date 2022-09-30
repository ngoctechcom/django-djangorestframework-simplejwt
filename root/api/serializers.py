from rest_framework import serializers
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Project
from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
