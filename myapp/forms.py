from django import forms
from .models import Apiary, Beekeeper, Beehive, Activity

#Forms examples
class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de tarea', max_length=200)
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea)

class CreateTaskActivity(forms.Form):
    title = forms.CharField(label='Titulo de tarea', max_length=200)
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)

#Forms project
class CreateApiary(forms.Form):
    name = forms.CharField(label="Nombre del Apiario", max_length=200)
    latitude = forms.FloatField(label='Latitud')
    longitude = forms.FloatField(label='Longitud')
    country = forms.CharField(label='Estado', max_length=200)
    city = forms.CharField(label='Ciudad', max_length=200)
    street = forms.CharField(label='Direccion', max_length=200)

class CreateBeekeeper(forms.Form):
    name = forms.CharField(label="Nombre del Apicultor", max_length=200)
    apiary = forms.CharField(label='Apiario', widget=forms.Select)
    email = forms.CharField(label='Email', max_length=200)
    phone = forms.CharField(label='Telefono', max_length=10)

class CreateBeehive(forms.Form):
    code_beehive = forms.CharField(label='Código de Colmena', max_length=100)
    #apiary = forms.CharField(label='Apiario')
    temperature = forms.CharField(label='Temperatura')
    specie = forms.CharField(label='Especie')


class CreateActivity(forms.Form):
    activity = forms.CharField(label='Actividad', max_length=200)
    description = forms.CharField(label='Descripcion de la actividad', widget=forms.Textarea)
    #apiary = forms.CharField(label='Apiario')
    #beehive = forms.CharField(label='Colmena')
    #beekeeper = forms.CharField(label='Apicultor')

class CreateBeekeeperModelForm(forms.ModelForm):
    apiary = forms.ModelChoiceField(queryset=Apiary.objects.all(), label='Apiario')
    
    class Meta:
        model = Beekeeper
        fields = ['name', 'apiary', 'email', 'phone']

class CreateBeehiveModelForm(forms.ModelForm):
    apiary = forms.ModelChoiceField(queryset=Apiary.objects.all(), label='Apiario')
    
    class Meta:
        model = Beehive
        fields = ['code_beehive', 'apiary', 'temperature', 'specie']

class CreateActivityModelForm(forms.ModelForm):
    apiary = forms.ModelChoiceField(queryset=Apiary.objects.all(), label='Apiario')
    beehive = forms.ModelChoiceField(queryset=Beehive.objects.all(), label='Colmena')
    beekeeper = forms.ModelChoiceField(queryset=Beekeeper.objects.all(), label='Apicultor')

    class Meta:
        model = Activity
        fields = ['activity', 'description','apiary', 'beehive', 'beekeeper']


