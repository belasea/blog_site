from django.db import models

class AboutInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    expertise = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=210, blank=True, null=True)
    resume = models.ImageField(upload_to="about_me/", blank=True, null=True)

    facebook_link = models.URLField("Facebook URL", blank=True, null=True)
    linkedin_link = models.URLField("LinkedIn URL", blank=True, null=True)
    github_link = models.URLField("GitHub URL", blank=True, null=True)
    instagram_link = models.URLField("Instagram URL", blank=True, null=True)
    profile = models.ImageField(upload_to="about_me/", blank=True, null=True)
    profile_text = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name or "Unnamed Profile"
    

class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    key_skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled About Section"


class AboutDetails(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='details')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description

class Experience(models.Model): 
    company_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    company_logo = models.ImageField(upload_to="experience/", blank=True, null=True)
    duration_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.position} at {self.company_name}" if self.position else self.company_name

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




class Footer(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    facebook_url = models.URLField(max_length=120, blank=True, null=True)
    github_url = models.URLField(max_length=120, blank=True, null=True)
    linkedin_url = models.URLField(max_length=120, blank=True, null=True)
    instagram_url = models.URLField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']