from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Contact, ContactInfo, ReplayContact



# Contact CSV import and Export ============================================================
class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        fields = ['id', 'subject', 'name', 'phone', 'email', 'message']


class ContactAdmin(ImportExportModelAdmin):
    resource_class = ContactResource
    list_display = ['name', 'phone', 'email']
    list_per_page = 20
    search_fields = ['phone', 'email',]


admin.site.register(Contact, ContactAdmin)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "address") 
    search_fields = ("email", "phone", "address")



# ReplayContactAdmin Admin ============================================================
class ReplayContactAdmin(admin.ModelAdmin):
    list_display = ["message"]
    
    class Meta:
        model = ReplayContact
        fields = ['id', 'message']
       
        
admin.site.register(ReplayContact, ReplayContactAdmin)