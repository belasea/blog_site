from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    url_link = models.URLField("Project URL", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title or "Untitled Project"



class MyService(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "My Service"
        verbose_name_plural = "My Services"

    def __str__(self):
        return self.title or "Unnamed Service"


class ServiceItem(models.Model):
    my_service = models.ForeignKey(MyService, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
