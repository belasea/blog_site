from django.contrib import admin
from .models import Project, MyService, ServiceItem


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)

@admin.register(MyService)
class MyServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    list_per_page = 10

@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('my_service', 'description')
    list_filter = ('my_service',)
    list_per_page = 10
