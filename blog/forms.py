
from django import forms
from django.forms import Textarea
from .models import Category, SubCategory,  Blog, Comment

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
        ]


class SubCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = [
            'title',
        ]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'category',
            'sub_category',
            'image',
            'facebook_url',
            'instagram_url',
            'github_url',
            'linkedin_url',
            'description',
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'approve']

        # Override the Customer some fields
        widgets = {
            'body': Textarea(attrs={'rows': 3, 'cols': 3}),
        }

