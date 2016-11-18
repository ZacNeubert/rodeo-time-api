from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Project, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        exclude = ('password', 'is_staff', 'is_superuser')

class ProjectSerializer(serializers.ModelSerializer):
    number_of_entries = serializers.SerializerMethodField()

    def get_number_of_entries(self, project):
        return project.entries.count()

    class Meta:
        model = Project
        fields = ('manager', 'members', 'name', 'description', 'updated', 'created', 'number_of_entries')
	depth = 1


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('user', 'project', 'hours', 'minutes', 'seconds', 'updated', 'created')
