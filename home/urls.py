from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog-detail'),
    path('category/<slug:slug>/', views.category_detail, name='category-detail'),

]