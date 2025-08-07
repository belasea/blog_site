from django.shortcuts import render
from .models import AboutInfo, About, AboutDetails, Experience, Project,  MyService

# Create your views here.

def home(request):
    about_info = AboutInfo.objects.order_by('-updated_at').first()
    services = MyService.objects.prefetch_related('items').all()
    projects = Project.objects.all()


    # Split expertise into a list (handles None safely)
    expertise_list = []
    if about_info and about_info.expertise:
        expertise_list = [skill.strip() for skill in about_info.expertise.split(',')]
    

    # Split expertise into a list (handles None safely)
    skills = About.objects.first()
    key_skills_list = []
    if skills and skills.key_skills:
        key_skills_list = [skill.strip() for skill in skills.key_skills.split(',')]
    
    about_details = AboutDetails.objects.all()


    experience = Experience.objects.all()
    # For each experience, split the description into lines
    for exp in experience:
        if exp.description:
            exp.description_list = [line.strip() for line in exp.description.strip().split('\n') if line.strip()]

    context = {
        'about_info': about_info,
        'projects': projects,
        'services': services,
        'expertise_list': expertise_list,
        'skills': skills,
        'key_skills_list': key_skills_list,
        'about_details': about_details,
        'experience': experience,
        # 'description_list': experience
    }
    return render(request, "home/index.html", context)
