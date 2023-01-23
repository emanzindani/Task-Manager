from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_list(request):
    projects = projects = Project.objects.filter(owner=request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)
