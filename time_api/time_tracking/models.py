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

class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    user = models.ForeignKey(User, related_name='time_entries')
    task = models.ForeignKey(Task, null=True)
    notes = models.TextField(null=True, blank=True)
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    time_in = models.DateTimeField()
    time_out = models.DateTimeField()

    def __str__(self):
        return '{} - {}:{}'.format(self.user, self.hours, self.minutes)
