from django.shortcuts import render
from .models import Project,  MyService

# Create your views here.

def home(request):
    services = MyService.objects.prefetch_related('items').all()
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'services': services 
    }
    return render(request, "home/index.html", context)
