from profile import Profile

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Project, Entry, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('manager', 'members', 'name', 'description', 'updated', 'created')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'updated', 'created')
        depth = 1


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('user', 'task', 'hours', 'minutes', 'seconds', 'updated', 'created', 'time_in', 'time_out')
