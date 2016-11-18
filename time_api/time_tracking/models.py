from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    manager = models.ForeignKey(User, related_name='managed_projects')
    members = models.ManyToManyField(User, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    user = models.ForeignKey(User, related_name='time_entries')
    project = models.ForeignKey(Project, related_name='entries')
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}:{}'.format(self.user, self.hours, self.minutes)
