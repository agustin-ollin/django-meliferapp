from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize

from . import models
from .models import Project, Task, Apiary, Beekeeper, Beehive, Activity
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject, CreateApiary, CreateActivity, CreateBeekeeper, CreateBeehive
from django.views.generic import TemplateView, CreateView, ListView, View, DetailView, DeleteView, UpdateView

# Class-based views for porject final

    
class ApiariesView(ListView):
    template_name = 'apiary/apiary.html'
    model = Apiary

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            apiarios = Apiary.objects.all()
            apiarios_serializados = serialize('json', apiarios)
            context['apiarios_serializados'] = apiarios_serializados
            return context

class CreateApiaryView(CreateView):
    form_class = CreateApiary
    model = Apiary
    template_name = 'apiary/create_apiary.html'

    def get(self, request, *args, **kwargs):
        contex = {'form': CreateApiary()}

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Apiary.objects.create(
                name=request.POST['name'],
                latitude=request.POST['latitude'],
                longitude=request.POST['longitude'],
                country=request.POST['country'],
                city=request.POST['city'],
                street=request.POST['street'],
            )
            return redirect("apiaries")

        return render(request, self.template_name, {"form": form})

class ApiaryDeleteView(DeleteView):
    template_name = 'apiary/delete_apiary.html'
    success_url = "/apiaries"
    model = Apiary

class ApiaryUpdateView(UpdateView):
    model = Apiary
    fields = ["name", "latitude", "longitude", "country", "city", "street"]
    template_name = 'apiary/update_apiary.html'
    success_url = "/apiaries"

class ApiaryDetailView(DetailView):
    template_name = 'apiary/detail_apiary.html'
    model = Apiary


class BeekeeperView(ListView):
    template_name = 'beekeeper/beekeeper.html'
    model = Beekeeper

class CreateBeekeeperView(CreateView):
    form_class = CreateBeekeeper
    model = Beekeeper
    template_name = 'beekeeper/create_beekeeper.html'

    def get(self, request, *args, **kwargs):
        contex = {'form': CreateBeekeeper()}

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Beekeeper.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                apiary_id=1
            )
            return redirect("beekeeper")

        return render(request, self.template_name, {"form": form})

class BeekeeperDeleteView(DeleteView):
    template_name = 'beekeeper/delete_beekeeper.html'
    success_url = "/beekeeper"
    model = Beekeeper

class BeekeeperUpdateView(UpdateView):
    model = Beekeeper
    fields = ["name", "apiary", "email", "phone"]
    template_name = 'beekeeper/update_beekeeper.html'
    success_url = "/beekeeper"

class BeeHiveView(ListView):
    template_name = 'beehive/beehive.html'
    model = Beehive

class CreateBeeHiveView(CreateView):
    form_class = CreateBeehive
    model = Beehive
    template_name = 'beehive/create_beehive.html'

    def get(self, request, *args, **kwargs):
        contex = {'form': CreateBeehive()}

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Beehive.objects.create(
                code_beehive=request.POST['code_beehive'],
                temperature=request.POST['temperature'],
                specie=request.POST['specie'],
                apiary_id=1
            )
            return redirect("beehive")

        return render(request, self.template_name, {"form": form})

class BeehiveDeleteView(DeleteView):
    template_name = 'beehive/delete_beehive.html'
    success_url = "/beehive"
    model = Beehive

class BeehiveUpdateView(UpdateView):
    model = Beehive
    fields = ["code_beehive", "apiary", "temperature", "specie"]
    template_name = 'beehive/update_beehive.html'
    success_url = "/beehive"


class ActivitiesView(ListView):
    template_name = 'activity/activities.html'
    model = Activity

class CreateActivityView(CreateView):
    form_class = CreateActivity
    model = Activity
    template_name = 'activity/create_activity.html'

    def get(self, request, *args, **kwargs):
        contex = {'form': CreateActivity()}

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Activity.objects.create(
                activity=request.POST['activity'],
                description=request.POST['description'],
                apiary_id=1,
                beehive_id=1,
                beekeeper_id=1,
            )
            return redirect("beehive")

        return render(request, self.template_name, {"form": form})

class ActivityDeleteView(DeleteView):
    template_name = 'activity/delete_activity.html'
    success_url = "/activities"
    model = Activity

class ActivityUpdateView(UpdateView):
    model = Activity
    fields = ["activity", "description", "apiary", "beehive", "beekeeper"]
    template_name = 'activity/update_activity.html'
    success_url = "/activities"


#############################
# Class-based views examples
#############################
class AboutView(TemplateView):
    template_name = 'about.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectsListViews(ListView):
    template_name = 'projects/projects.html'
    model = Project


class TasksListViews(ListView):
    template_name = 'tasks/tasks.html'
    model = Task


class HelloView(View):
    def get(self, request, username):
        return HttpResponse("<h1>Hello World %s</h1>" % username)


class CreateProjectView(CreateView):
    form_class = CreateNewProject
    model = Project
    template_name = 'projects/create_project.html'

    def get(self, request, *args, **kwargs):
        contex = {'form': CreateNewProject()}

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Project.objects.create(name=request.POST['name'])
            return redirect("projects")

        return render(request, self.template_name, {"form": form})


class CreateTaskView(CreateView):
    form_class = CreateNewTask
    template_name = 'tasks/create_task.html'
    initial = {
        "title": "", "description": "", "project": ""
    }

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Task.objects.create(title=request.POST['title'], description=request.POST['description'],
                                project_id=request.POST['project'])
            return redirect("tasks")

        return render(request, self.template_name, {"form": form})


class TaskDetailView(DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task


class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = Project

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(project_id=self.kwargs['pk'])
        return render(request, self.template_name,
                      {"tasks": tasks, "project": models.Project.objects.get(pk=self.kwargs['pk'])})


class ProjectDeleteView(DeleteView):
    template_name = 'projects/delete_project.html'
    success_url = "/projects"
    model = Project


class TaskDeleteView(DeleteView):
    template_name = 'tasks/delete_task.html'
    success_url = "/tasks"
    model = Task


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ["name"]
    template_name = 'projects/update_project.html'
    success_url = "/projects"


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "project"]
    template_name = 'tasks/update_task.html'
    success_url = "/tasks"
