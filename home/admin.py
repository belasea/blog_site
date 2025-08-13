from django.contrib import admin
from .models import (
    MyInfo, 
    About, 
    AboutDetail, 
    Project, 
    MyService, 
    ServiceItem,
    Experience,
    Footer,
    Header
)


@admin.register(MyInfo)
class MyInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(AboutDetail)
class AboutDetailAdmin(admin.ModelAdmin):
    list_display = ("about",)
    search_fields = ("about",)


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


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'timestamp', 'update')
    search_fields = ('name', 'phone', 'email')
    ordering = ('-timestamp',)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email', 'timestamp', 'update')
    search_fields = ('title', 'phone', 'email')
    ordering = ('-timestamp',)

