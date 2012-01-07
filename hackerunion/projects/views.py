from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from projects.models import Project


def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return HttpResponse('Project: %r' % project)


@login_required
def new_project(request):
    if request.user.projects.filter(is_active=True).exists():
        return HttpResponse('You may only have 1 active project at a time.')
    return HttpResponse('Will show project creation form.')
