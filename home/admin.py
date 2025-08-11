from django.contrib import admin
from .models import (
    AboutInfo, 
    About, 
    AboutDetails, 
    Project, 
    MyService, 
    ServiceItem,
    Experience,
)




@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(AboutDetails)
class AboutDetailsAdmin(admin.ModelAdmin):
    list_display = ("description", "about")
    search_fields = ("description",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company_name",)
    search_fields = ("company_name",)

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

