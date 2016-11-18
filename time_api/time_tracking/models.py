from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    manager = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    PROFILE_TYPES = (
        ('MN', 'Manager'),
        ('WB', 'WaterBoy'),
        ('UI', 'Unpaid Intern'),
        ('SD', 'Senior Developer'),
        ('NO', 'Nobody')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_type = models.CharField(
        max_length=2,
        choices=PROFILE_TYPES,
        default='NO',
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user)

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
