from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Project, Entry, Task, Profile
from .serializers import ProjectSerializer, EntrySerializer, TaskSerializer, ProfileSerializer, UserSerializer, UserCreateSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
