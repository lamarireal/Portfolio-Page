from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, translate_url
from django.utils.translation import get_language
from django.utils.translation import gettext as _

from .models import ChronologyEntry, Project, Skill


def get_language_options(request):
    current_language = get_language()
    return [
        {
            "code": code,
            "name": name,
            "url": translate_url(request.get_full_path(), code),
            "is_active": code == current_language,
        }
        for code, name in settings.LANGUAGES
    ]


# Create your views here.
def index(request):
    all_projects = Project.objects.all().order_by('-pub_date')
    chronology_entries = ChronologyEntry.objects.all().order_by('date_label')
    all_skills = Skill.objects.all().order_by('order')
    context = {
        "all_projects": all_projects,
        "chronology_entries": chronology_entries,
        "all_skills": all_skills,
        "language_options": get_language_options(request),
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
        return render(request, 'mainapp/project_details.html', {
            'error': _('Project not found.'),
            'back_url': back_url,
            'language_options': get_language_options(request),
        })

    context = {
        "project": project,
        "back_url": back_url,
        "language_options": get_language_options(request),
    }
    return render(request, 'mainapp/project_details.html', context)

def my_library(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project": project}
    return render(request, 'mainapp/my_library.html', context)
