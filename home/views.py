from django.shortcuts import render, redirect, get_object_or_404
from blog_site.local_settings import BASE_URL
from notification.models import Notification
from blog.models import Blog
from blog.forms import CommentForm
from contacts.forms import ContactForm
from .models import (
    AboutInfo, 
    About, 
    AboutDetails, 
    Experience, 
    Project,  
    MyService
)
from django.contrib import messages
# Create your views here.

def home(request):
    about_info = AboutInfo.objects.order_by('-updated_at').first()
    services = MyService.objects.prefetch_related('items').all()
    projects = Project.objects.all()
    blog = Blog.objects.order_by('-timestamp')[:4]


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
            exp.description_list = [line.strip() for line in exp.description.strip().split('\n')
             if line.strip()]
    

    form = ContactForm(request.POST or None)
    errors = None
    
    if request.method == 'POST':
        if form.is_valid():
            subject = form.cleaned_data['subject']
            form.save()
            messages.add_message(request, messages.SUCCESS, "Success! Thank you for your message.")
            # Create a notification for the user
            notification_message = f'Created : {subject}'
            try:
                # Set the appropriate link if needed
                link = BASE_URL + "/contact-list"
            except:
                link = None
            notification = Notification(user=request.user, message=notification_message, link=link)
            notification.save()
            return redirect('home')
        else:
            errors = form.errors

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
        'blog': blog,
        'form': form,
        'errors': errors
    }
    return render(request, "home/index.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    recent_post = Blog.objects.all().order_by('-timestamp')[:3]
    comments = post.comments.filter(approve=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            messages.add_message(request, messages.SUCCESS, "Comment successfully sent, Thanks")
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'object': post,
        'recent_post': recent_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, "blog/details.html", context)

