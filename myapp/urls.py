from django.urls import path
from . import views
from django.views.generic import TemplateView
from .formsets import FormsetProject, FormsetBeekeeper, FormsetTask

urlpatterns = [
    path('', views.ApiariesView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('hello/<str:username>', views.HelloView.as_view(), name="hello"),
    path('projects/', views.ProjectsListViews.as_view(), name="projects"),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name="project_detail"),
    path('projects/delete/<int:pk>', views.ProjectDeleteView.as_view(), name="project_delete"),
    path('projects/update/<int:pk>', views.ProjectUpdateView.as_view(), name="project_update"),
    path('tasks/', views.TasksListViews.as_view(), name="tasks"),
    path('tasks/<pk>/', views.TaskDetailView.as_view(), name="task_detail"),
    path('tasks/delete/<int:pk>', views.TaskDeleteView.as_view(), name="task_delete"),
    path('tasks/update/<int:pk>', views.TaskUpdateView.as_view(), name="task_update"),
    path('create_task/', views.CreateTaskView.as_view(), name="create_task"),
    path('create_project/', views.CreateProjectView.as_view(), name="create_project"),
    path('crear_project_formset/', FormsetProject.as_view(), name="crear_project_formset"),

    path('apiaries/', views.ApiariesView.as_view(), name="apiaries"),
    path('create_apiary/', views.CreateApiaryView.as_view(), name="create_apiary"),
    path('apiaries/<int:pk>/', views.ApiaryDetailView.as_view(), name="apiary_detail"),
    path('apiaries/delete/<int:pk>', views.ApiaryDeleteView.as_view(), name="apiary_delete"),
    path('apiaries/update/<int:pk>', views.ApiaryUpdateView.as_view(), name="apiary_update"),
    path('create_beekeeper_formset/', FormsetBeekeeper.as_view(), name="create_beekeeper_formset"),

    path('beehive/', views.BeeHiveView.as_view(), name="beehive"),
    path('create_beehive/', views.CreateBeeHiveView.as_view(), name="create_beehive"),
    path('beehive/delete/<int:pk>', views.BeehiveDeleteView.as_view(), name="beehive_delete"),
    path('beehive/update/<int:pk>', views.BeehiveUpdateView.as_view(), name="beehive_update"),

    path('beekeeper/', views.BeekeeperView.as_view(), name="beekeeper"),
    path('create_beekeeper/', views.CreateBeekeeperView.as_view(), name="create_beekeeper"),
    path('beekeeper/delete/<int:pk>', views.BeekeeperDeleteView.as_view(), name="beekeeper_delete"),
    path('beekeeper/update/<int:pk>', views.BeekeeperUpdateView.as_view(), name="beekeeper_update"),

    path('activities/', views.ActivitiesView.as_view(), name="activities"),
    path('create_activity/', views.CreateActivityView.as_view(), name="create_activity"),
    path('activity/delete/<int:pk>', views.ActivityDeleteView.as_view(), name="activity_delete"),
    path('activity/update/<int:pk>', views.ActivityUpdateView.as_view(), name="activity_update"),
    path('crear_tarea/<int:pk>', FormsetTask.as_view(), name='crear_tarea')
]
