from django import forms
from django.forms import inlineformset_factory
from .models import Profile, Experience, Education, Skill, Project

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 (555) 123-4567'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Your Address'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://yourwebsite.com'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/yourprofile'}),
            'github': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/yourusername'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Brief professional summary...'}),
            'template_choice': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 250, 'value': 1}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['profile']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jan 2020'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Present'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Job responsibilities and achievements...'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['profile']
        widgets = {
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University Name'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bachelor of Science'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Computer Science'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2018'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2022'}),
            'gpa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3.8/4.0'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['profile']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python'}),
            'proficiency': forms.Select(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Project description...'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, JavaScript'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username/project'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jan 2023'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mar 2023'}),
        }

# Formsets for dynamic forms
ExperienceFormSet = inlineformset_factory(Profile, Experience, form=ExperienceForm, extra=2, can_delete=True)
EducationFormSet = inlineformset_factory(Profile, Education, form=EducationForm, extra=1, can_delete=True)
SkillFormSet = inlineformset_factory(Profile, Skill, form=SkillForm, extra=5, can_delete=True)
ProjectFormSet = inlineformset_factory(Profile, Project, form=ProjectForm, extra=2, can_delete=True)
