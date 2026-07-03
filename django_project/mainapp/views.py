from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import ChronologyEntry, Project, Skill


# Create your views here.
def index(request):
    all_projects = Project.objects.all().order_by('-pub_date')
    chronology_entries = ChronologyEntry.objects.all().order_by('date_label')
    all_skills = Skill.objects.all().order_by('order')
    context = {
        "all_projects": all_projects,
        "chronology_entries": chronology_entries,
        "all_skills": all_skills,
    }
    return render(request, 'mainapp/index.html', context)

def project_detail(request, project_id):
    return_to = request.GET.get('from', '')
    back_url = reverse('mainapp:index')
    if return_to:
        back_url = f"{reverse('mainapp:index')}#{return_to}"

    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return render(request, 'mainapp/project_details.html', {'error': 'Project not found.', 'back_url': back_url})

    context = {"project": project, "back_url": back_url}
    return render(request, 'mainapp/project_details.html', context)

def my_library(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project": project}
    return render(request, 'mainapp/my_library.html', context)
