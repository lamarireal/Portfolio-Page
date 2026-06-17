from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('my_library/<int:project_id>/', views.my_library, name='my_library'),
]