from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from projects.models import Project


def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return HttpResponse('Project: %r' % project)
