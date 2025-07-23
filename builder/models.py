from django.db import models
from django.urls import reverse


class Profile(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100, blank=True)  # made optional
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    # Professional Summary
    summary = models.TextField(max_length=500, help_text="Professional summary", blank=True)  # optional

    # Template Choice
    template_choice = models.IntegerField(default=1, help_text="Template number (1-250)")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name or "Unnamed Profile"

    def get_absolute_url(self):
        return reverse('preview', kwargs={'pk': self.pk})


class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=True)  # optional
    position = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True, default="Present")
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position or 'No Position'} at {self.company or 'No Company'}"


class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    gpa = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree or 'No Degree'} from {self.institution or 'Unknown Institution'}"


class Skill(models.Model):
    profile = models.ForeignKey(Profile, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    proficiency = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ], default='Intermediate', blank=True)

    def __str__(self):
        return self.name or "Unnamed Skill"


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=300, blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name or "Unnamed Project"
