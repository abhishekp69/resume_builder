from django.contrib import admin
from .models import Profile, Experience, Education, Skill, Project

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'template_choice', 'created_at']
    list_filter = ['template_choice', 'created_at']
    search_fields = ['full_name', 'email']
    inlines = [ExperienceInline, EducationInline, SkillInline, ProjectInline]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['profile', 'company', 'position', 'start_date', 'end_date']
    list_filter = ['company', 'start_date']
    search_fields = ['profile__full_name', 'company', 'position']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['profile', 'institution', 'degree', 'start_date', 'end_date']
    list_filter = ['institution', 'degree']
    search_fields = ['profile__full_name', 'institution', 'degree']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['profile', 'name', 'proficiency']
    list_filter = ['proficiency']
    search_fields = ['profile__full_name', 'name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['profile', 'name', 'technologies', 'start_date']
    search_fields = ['profile__full_name', 'name', 'technologies']
