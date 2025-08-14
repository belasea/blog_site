from django.shortcuts import render, redirect, get_object_or_404
from blog_site.local_settings import BASE_URL
from django.contrib import messages
from notification.models import Notification
from blog.models import Blog, Category
from blog.forms import CommentForm
from contacts.models import ContactInfo
from contacts.forms import ContactForm
from .models import (
    MyInfo, 
    About, 
    AboutDetail, 
    Experience, 
    Project, 
    MyService
)


def home(request):
    """
    Render the home page with personal information, projects, services,
    skills, experiences, recent blog posts, and a contact form.

    - Retrieves the latest `MyInfo` record for about info.
    - Fetches contact information and available services.
    - Retrieves all projects and the latest 4 blog posts.
    - Splits `expertise` and `key_skills` fields into lists for display.
    - Loads about details and work experiences, splitting experience
      descriptions into line-by-line lists.
    - Handles contact form submission:
        - Saves the contact message.
        - Creates a notification for the user.
        - Displays a success message.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "home/index.html" page.
    """
    about_info = MyInfo.objects.order_by('-updated_at').first()
    contact_info = ContactInfo.objects.first()
    services = MyService.objects.prefetch_related('items').all()
    projects = Project.objects.all()
    blog = Blog.objects.order_by('-timestamp')[:4]

    # Split expertise into a list (handles None safely)
    expertise_list = []
    if about_info and about_info.expertise:
        expertise_list = [skill.strip() for skill in about_info.expertise.split(',')]

    # Split key skills into a list (handles None safely)
    skills = About.objects.first()
    key_skills_list = []
    if skills and skills.key_skills:
        key_skills_list = [skill.strip() for skill in skills.key_skills.split(',')]

    about_details = AboutDetail.objects.all()

    # Process experience descriptions into line-separated lists
    experience = Experience.objects.all()
    for exp in experience:
        if exp.description:
            exp.description_list = [
                line.strip() for line in exp.description.strip().split('\n') if line.strip()
            ]

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
                link = BASE_URL + "/contact-list"
            except:
                link = None
            Notification.objects.create(user=request.user, message=notification_message, link=link)
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
        'blog': blog,
        'form': form,
        'errors': errors,
        'contact_info': contact_info,
    }
    return render(request, "home/index.html", context)


def skills(request):
    return render(request, "home/skills.html") 


def blog_detail(request, slug):
    """
    Display a detailed view of a single blog post, along with recent posts and comments.

    - Retrieves the blog post matching the provided slug.
    - Loads the 3 most recent blog posts for sidebar display.
    - Fetches approved comments for the current post.
    - Handles new comment submission:
        - Validates and saves the comment.
        - Associates it with the current post.
        - Shows a success message.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the blog post to display.

    Returns:
        HttpResponse: The rendered "blog/details.html" page.
    """
    post = get_object_or_404(Blog, slug=slug)

    # 3 most recent posts (already in your code)
    recent_post = Blog.objects.all().order_by('-timestamp')[:3]

    # Get posts from the same category (excluding the current one)
    related_posts = Blog.objects.filter(
        category=post.category
    ).exclude(id=post.id)[:4]  # Limit to 4 related posts
    # All categories for sidebar
    categories = Category.objects.all().order_by('title')
    comments = post.comments.filter(approve=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            messages.add_message(request, messages.SUCCESS, "Comment successfully sent, Thanks")
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'object': post,
        'recent_post': recent_post,
        'related_posts': related_posts,
        'categories': categories,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, "blog/details.html", context)


def category_detail(request, slug):
    # Get the category
    category = get_object_or_404(Category, slug=slug)

    # Get all blogs in this category
    blogs = Blog.objects.filter(category=category)

    # Optionally, get all categories for sidebar/navigation
    categories = Category.objects.all()

    context = {
        'category': category,
        'blogs': blogs,
        'categories': categories,  # pass all categories
    }
    return render(request, "blog/category_detail.html", context)
