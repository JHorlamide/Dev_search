from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name='projects'),
    path('<uuid:pk>/', views.project, name='project'),
    path('create_project/', views.create_project, name='create_project'),
    path('update/<uuid:projectId>/', views.updateProject, name='update_project'),
    path('delete/<uuid:projectId>/', views.deleteProject, name='delete_project'),
    path('add-review/<uuid:projectId>/', views.deleteProject, name='delete_project'),
]
