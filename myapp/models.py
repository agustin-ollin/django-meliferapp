from django.db import models

# Model for project
class Apiary(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Beekeeper(models.Model):
    name = models.CharField(max_length=100)
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Beehive(models.Model):
    code_beehive = models.CharField(max_length=100)
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE)
    temperature = models.FloatField()
    specie = models.CharField(max_length=100)

    def __str__(self):
        return self.code_beehive

class Activity(models.Model):
    activity = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE)
    beehive = models.ForeignKey(Beehive, on_delete=models.CASCADE)
    beekeeper = models.ForeignKey(Beekeeper, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name
