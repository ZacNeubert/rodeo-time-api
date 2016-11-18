from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render

from .models import Entry, Project


def entry_list(request):
    all_entries = Entry.objects.all()

    return render(request, 'entries/entry_list.html', {'entries': all_entries})


class ProjectList(ListView):
    model = Project


class ProjectDetail(DetailView):
    queryset = Project.objects.all()


class ProjectCreate(CreateView):
    model = Project
    success_url = '/projects/'
    fields = ['manager', 'members', 'name', 'description']


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['manager', 'members', 'name', 'description']

    def get_success_url(self):
        return '/projects/{}/'.format(self.object.id)
