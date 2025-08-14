from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, SubCategory, Blog, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'timestamp', 'update')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'timestamp', 'update')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  # Summernote editor
    list_display = ('title', 'category', 'sub_category', 'timestamp', 'update')
    search_fields = ('title', 'category__title', 'sub_category__title')
    list_filter = ('category', 'sub_category', 'timestamp')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'approve', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_filter = ('approve', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approve=True)
