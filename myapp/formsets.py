from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from myapp.models import Project, Beekeeper
from myapp.forms import CreateNewProject, CreateBeekeeper


class FormsetProject(FormView):
    template_name = 'projects/project_formset.html'
    success_url = '/projects'
    form_class = formset_factory(CreateNewProject, extra=1)

    def form_valid(self, form):
        for f in form:
            Project.objects.create(name=f.cleaned_data['name'])
        return super(FormsetProject, self).form_valid(form)


class FormsetBeekeeper(FormView):
    template_name = 'apiary/apiaries_formset.html'
    success_url = '/apiaries'
    form_class = formset_factory(CreateBeekeeper, extra=1)

    def form_valid(self, form):
        for f in form:
            Beekeeper.objects.create(name=f.cleaned_data['name'], email=f.cleaned_data['email'],
                                     phone=f.cleaned_data['phone'], apiary_id=1)
        return super(FormsetBeekeeper, self).form_valid(form)
