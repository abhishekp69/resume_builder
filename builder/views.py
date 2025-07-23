from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.contrib import messages
from django.urls import reverse
from .models import Profile
from .forms import (
    ProfileForm, ExperienceFormSet, EducationFormSet, 
    SkillFormSet, ProjectFormSet
)

try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
    PDF_ENABLED = True
except ImportError:
    PDF_ENABLED = False


def index(request):
    """Home page with resume builder form"""
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        experience_formset = ExperienceFormSet(request.POST)
        education_formset = EducationFormSet(request.POST)
        skill_formset = SkillFormSet(request.POST)
        project_formset = ProjectFormSet(request.POST)

        if (profile_form.is_valid() and experience_formset.is_valid() and 
            education_formset.is_valid() and skill_formset.is_valid() and 
            project_formset.is_valid()):

            profile = profile_form.save()

            experience_formset.instance = profile
            experience_formset.save()

            education_formset.instance = profile
            education_formset.save()

            skill_formset.instance = profile
            skill_formset.save()

            project_formset.instance = profile
            project_formset.save()

            messages.success(request, 'Resume created successfully!')
            return redirect('preview', pk=profile.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        profile_form = ProfileForm()
        experience_formset = ExperienceFormSet()
        education_formset = EducationFormSet()
        skill_formset = SkillFormSet()
        project_formset = ProjectFormSet()

    context = {
        'profile_form': profile_form,
        'experience_formset': experience_formset,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset,
    }

    return render(request, 'builder/index.html', context)

def preview(request, pk):
    """Preview the generated resume"""
    profile = get_object_or_404(Profile, pk=pk)

    # Ensure template choice is within valid range
    template_num = max(1, min(250, profile.template_choice))

    template_name = f'builder/templates/resume_{template_num}.html'

    context = {
        'profile': profile,
        'template_num': template_num,
        'pdf_enabled': PDF_ENABLED,
    }

    try:
        return render(request, template_name, context)
    except:
        # Fallback to template 1 if specific template doesn't exist
        return render(request, 'builder/templates/resume_1.html', context)

def download_pdf(request, pk):
    """Download resume as PDF"""
    if not PDF_ENABLED:
        messages.error(request, 'PDF export is not available. Please install WeasyPrint.')
        return redirect('preview', pk=pk)

    profile = get_object_or_404(Profile, pk=pk)
    template_num = max(1, min(250, profile.template_choice))

    template_name = f'builder/templates/resume_{template_num}.html'

    context = {
        'profile': profile,
        'template_num': template_num,
        'is_pdf': True,  # Flag to modify template for PDF
    }

    try:
        html_string = render_to_string(template_name, context, request=request)
    except:
        html_string = render_to_string('builder/templates/resume_1.html', context, request=request)

    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    # Create PDF
    pdf = html.write_pdf()

    # Create response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.full_name}_Resume.pdf"'

    return response

def template_gallery(request):
    """Display template gallery"""
    templates = [{'id': i, 'name': f'Template {i}'} for i in range(1, 251)]
    return render(request, 'builder/gallery.html', {'templates': templates})

def edit_resume(request, pk):
    """Edit existing resume"""
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        experience_formset = ExperienceFormSet(request.POST, instance=profile)
        education_formset = EducationFormSet(request.POST, instance=profile)
        skill_formset = SkillFormSet(request.POST, instance=profile)
        project_formset = ProjectFormSet(request.POST, instance=profile)

        if (profile_form.is_valid() and experience_formset.is_valid() and 
            education_formset.is_valid() and skill_formset.is_valid() and 
            project_formset.is_valid()):

            profile_form.save()
            experience_formset.save()
            education_formset.save()
            skill_formset.save()
            project_formset.save()

            messages.success(request, 'Resume updated successfully!')
            return redirect('preview', pk=profile.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        profile_form = ProfileForm(instance=profile)
        experience_formset = ExperienceFormSet(instance=profile)
        education_formset = EducationFormSet(instance=profile)
        skill_formset = SkillFormSet(instance=profile)
        project_formset = ProjectFormSet(instance=profile)

    context = {
        'profile_form': profile_form,
        'experience_formset': experience_formset,
        'education_formset': education_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset,
        'profile': profile,
        'is_edit': True,
    }

    return render(request, 'builder/index.html', context)
