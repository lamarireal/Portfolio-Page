from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    all_projects = Project.objects.all().order_by('-pub_date')
    context = {"all_projects": all_projects}
    return render(request, 'mainapp/index.html', context)

def project_detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return render(request, 'mainapp/project_details.html', {'error': 'Project not found.'})
    context = {"project": project}
    return render(request, 'mainapp/project_details.html', context)

def my_library(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project": project}
    return render(request, 'mainapp/my_library.html', context)
