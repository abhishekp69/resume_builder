from django.core.management.base import BaseCommand
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Generate 250 resume templates'

    def handle(self, *args, **options):
        template_dir = os.path.join(settings.BASE_DIR, 'builder', 'templates', 'builder', 'templates')
        os.makedirs(template_dir, exist_ok=True)

        # Color schemes for templates
        color_schemes = [
            {'primary': '#2c3e50', 'secondary': '#3498db', 'accent': '#e74c3c'},
            {'primary': '#8e44ad', 'secondary': '#9b59b6', 'accent': '#f39c12'},
            {'primary': '#27ae60', 'secondary': '#2ecc71', 'accent': '#e67e22'},
            {'primary': '#e74c3c', 'secondary': '#c0392b', 'accent': '#f1c40f'},
            {'primary': '#34495e', 'secondary': '#2c3e50', 'accent': '#1abc9c'},
            {'primary': '#16a085', 'secondary': '#1abc9c', 'accent': '#f39c12'},
            {'primary': '#2980b9', 'secondary': '#3498db', 'accent': '#e74c3c'},
            {'primary': '#8e44ad', 'secondary': '#9b59b6', 'accent': '#e67e22'},
            {'primary': '#d35400', 'secondary': '#e67e22', 'accent': '#f1c40f'},
            {'primary': '#7f8c8d', 'secondary': '#95a5a6', 'accent': '#e74c3c'},
        ]

        for i in range(1, 251):
            color_scheme = color_schemes[(i-1) % len(color_schemes)]
            template_content = self.generate_template(i, color_scheme)

            template_path = os.path.join(template_dir, f'resume_{i}.html')
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(template_content)

            if i % 50 == 0:
                self.stdout.write(f'Generated {i} templates...')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully generated 250 resume templates!')
        )

    def generate_template(self, template_num, color_scheme):
        layouts = ['modern', 'classic', 'minimal', 'creative', 'professional']
        layout = layouts[(template_num-1) % len(layouts)]

        return f"""
{{% extends 'builder/base.html' %}}
{{% load static %}}

{{% block title %}}{{{{ profile.full_name }}}} - Resume Template {template_num}{{% endblock %}}

{{% block extra_css %}}
<style>
:root {{
    --primary-color: {color_scheme['primary']};
    --secondary-color: {color_scheme['secondary']};
    --accent-color: {color_scheme['accent']};
    --text-color: #333;
    --light-bg: #f8f9fa;
}}

.resume-container {{
    max-width: 800px;
    margin: 0 auto;
    background: white;
    min-height: 100vh;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    font-family: 'Segoe UI', sans-serif;
}}

/* {layout.title()} Layout Styles */
.resume-header {{
    background: {'linear-gradient(135deg, var(--primary-color), var(--secondary-color))' if layout == 'modern' else 'var(--primary-color)'};
    color: white;
    padding: {'3rem' if layout == 'creative' else '2rem'};
    text-align: {'left' if layout == 'professional' else 'center'};
    {'border-radius: 15px 15px 0 0;' if layout == 'modern' else ''}
}}

.resume-header h1 {{
    font-size: {'3rem' if layout == 'creative' else '2.5rem'};
    margin-bottom: 0.5rem;
    font-weight: {'300' if layout == 'minimal' else '700'};
    {'text-transform: uppercase;' if layout == 'professional' else ''}
    {'letter-spacing: 2px;' if layout == 'creative' else ''}
}}

.contact-info {{
    display: flex;
    flex-wrap: wrap;
    justify-content: {'flex-start' if layout == 'professional' else 'center'};
    gap: 1rem;
    margin-top: 1rem;
}}

.contact-item {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    {'background: rgba(255,255,255,0.1);' if layout == 'modern' else ''}
    {'padding: 0.5rem;' if layout == 'modern' else ''}
    {'border-radius: 5px;' if layout == 'modern' else ''}
}}

.resume-body {{
    padding: 2rem;
    {'display: grid; grid-template-columns: 1fr 2fr; gap: 2rem;' if layout == 'creative' else ''}
}}

.section {{
    margin-bottom: {'3rem' if layout == 'creative' else '2rem'};
}}

.section-title {{
    color: var(--primary-color);
    font-size: {'1.5rem' if layout == 'creative' else '1.3rem'};
    font-weight: {'400' if layout == 'minimal' else '600'};
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: {'none' if layout == 'minimal' else '2px solid var(--accent-color)'};
    {'background: var(--light-bg);' if layout == 'modern' else ''}
    {'padding: 1rem;' if layout == 'modern' else ''}
    {'border-radius: 5px;' if layout == 'modern' else ''}
    {'text-transform: uppercase;' if layout == 'professional' else ''}
}}

.experience-item, .education-item, .project-item {{
    margin-bottom: 1.5rem;
    padding: {'0' if layout == 'minimal' else '1rem'};
    {'border-left: 3px solid var(--accent-color);' if layout != 'minimal' else ''}
    background: {'none' if layout == 'minimal' else 'var(--light-bg)'};
    {'border-radius: 8px;' if layout == 'modern' else ''}
    {'box-shadow: 0 2px 5px rgba(0,0,0,0.05);' if layout == 'modern' else ''}
}}

.item-header {{
    display: flex;
    justify-content: space-between;
    align-items: {'center' if layout == 'professional' else 'flex-start'};
    margin-bottom: 0.5rem;
    {'flex-direction: column;' if layout == 'minimal' else ''}
    {'align-items: flex-start;' if layout == 'minimal' else ''}
}}

.item-title {{
    font-weight: {'500' if layout == 'minimal' else '600'};
    color: var(--text-color);
    {'font-size: 1.1rem;' if layout == 'creative' else ''}
}}

.item-company {{
    color: var(--primary-color);
    font-weight: 500;
    {'font-style: italic;' if layout == 'creative' else ''}
}}

.item-date {{
    color: #666;
    font-size: 0.9rem;
    {'background: var(--accent-color);' if layout == 'modern' else ''}
    {'color: white;' if layout == 'modern' else ''}
    {'padding: 0.25rem 0.5rem;' if layout == 'modern' else ''}
    {'border-radius: 3px;' if layout == 'modern' else ''}
}}

.skills-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax({'150px' if layout == 'minimal' else '200px'}, 1fr));
    gap: {'0.5rem' if layout == 'minimal' else '1rem'};
}}

.skill-item {{
    background: {'none' if layout == 'minimal' else 'var(--light-bg)'};
    padding: {'0.5rem' if layout == 'minimal' else '0.75rem'};
    {'border-radius: 5px;' if layout != 'minimal' else ''}
    {'border-left: 3px solid var(--accent-color);' if layout != 'minimal' else ''}
    {'border: 1px solid var(--accent-color);' if layout == 'minimal' else ''}
    {'text-align: center;' if layout == 'creative' else ''}
}}

.skill-name {{
    font-weight: {'400' if layout == 'minimal' else '500'};
    color: var(--text-color);
}}

.skill-level {{
    color: var(--primary-color);
    font-size: 0.9rem;
    {'display: block;' if layout == 'creative' else ''}
    {'margin-top: 0.25rem;' if layout == 'creative' else ''}
}}

/* Responsive Design */
@media (max-width: 768px) {{
    .resume-header {{
        padding: 1.5rem;
        text-align: center;
    }}

    .resume-header h1 {{
        font-size: 2rem;
    }}

    .contact-info {{
        flex-direction: column;
        align-items: center;
    }}

    .item-header {{
        flex-direction: column;
        align-items: flex-start;
    }}

    .skills-grid {{
        grid-template-columns: 1fr;
    }}

    .resume-body {{
        padding: 1rem;
        display: block;
    }}
}}

@media print {{
    .resume-container {{
        box-shadow: none;
        max-width: none;
    }}

    .section {{
        break-inside: avoid;
    }}
}}
</style>
{{% endblock %}}

{{% block content %}}
<div class="resume-container">
    <!-- Header Section -->
    <div class="resume-header">
        <h1>{{{{ profile.full_name }}}}</h1>
        {'<p style="font-size: 1.2rem; margin-bottom: 1rem;">Professional Resume</p>' if layout != 'minimal' else ''}
        <div class="contact-info">
            <div class="contact-item">
                <i class="bi bi-envelope"></i>
                <span>{{{{ profile.email }}}}</span>
            </div>
            <div class="contact-item">
                <i class="bi bi-telephone"></i>
                <span>{{{{ profile.phone }}}}</span>
            </div>
            {{% if profile.address %}}
            <div class="contact-item">
                <i class="bi bi-geo-alt"></i>
                <span>{{{{ profile.address }}}}</span>
            </div>
            {{% endif %}}
            {{% if profile.website %}}
            <div class="contact-item">
                <i class="bi bi-globe"></i>
                <a href="{{{{ profile.website }}}}" target="_blank" style="color: white;">Website</a>
            </div>
            {{% endif %}}
            {{% if profile.linkedin %}}
            <div class="contact-item">
                <i class="bi bi-linkedin"></i>
                <a href="{{{{ profile.linkedin }}}}" target="_blank" style="color: white;">LinkedIn</a>
            </div>
            {{% endif %}}
            {{% if profile.github %}}
            <div class="contact-item">
                <i class="bi bi-github"></i>
                <a href="{{{{ profile.github }}}}" target="_blank" style="color: white;">GitHub</a>
            </div>
            {{% endif %}}
        </div>
    </div>

    <!-- Body Section -->
    <div class="resume-body">
        {'<div class="main-content">' if layout == 'creative' else ''}

        <!-- Professional Summary -->
        {{% if profile.summary %}}
        <div class="section">
            <h2 class="section-title">{'Profile' if layout == 'minimal' else 'Professional Summary'}</h2>
            <p style="{'font-style: italic;' if layout == 'creative' else ''}">{{{{ profile.summary }}}}</p>
        </div>
        {{% endif %}}

        <!-- Experience -->
        {{% if profile.experiences.all %}}
        <div class="section">
            <h2 class="section-title">{'Experience' if layout == 'minimal' else 'Work Experience'}</h2>
            {{% for experience in profile.experiences.all %}}
            <div class="experience-item">
                <div class="item-header">
                    <div>
                        <div class="item-title">{{{{ experience.position }}}}</div>
                        <div class="item-company">{{{{ experience.company }}}}</div>
                    </div>
                    <div class="item-date">{{{{ experience.start_date }}}} - {{{{ experience.end_date }}}}</div>
                </div>
                <p>{{{{ experience.description }}}}</p>
            </div>
            {{% endfor %}}
        </div>
        {{% endif %}}

        {'</div><div class="sidebar">' if layout == 'creative' else ''}

        <!-- Education -->
        {{% if profile.education.all %}}
        <div class="section">
            <h2 class="section-title">Education</h2>
            {{% for education in profile.education.all %}}
            <div class="education-item">
                <div class="item-header">
                    <div>
                        <div class="item-title">{{{{ education.degree }}}} {'in' if education.field_of_study else ''} {{{{ education.field_of_study }}}}</div>
                        <div class="item-company">{{{{ education.institution }}}}</div>
                    </div>
                    <div class="item-date">{{{{ education.start_date }}}} - {{{{ education.end_date }}}}</div>
                </div>
                {{% if education.gpa %}}
                <p>GPA: {{{{ education.gpa }}}}</p>
                {{% endif %}}
            </div>
            {{% endfor %}}
        </div>
        {{% endif %}}

        <!-- Skills -->
        {{% if profile.skills.all %}}
        <div class="section">
            <h2 class="section-title">Skills</h2>
            <div class="skills-grid">
                {{% for skill in profile.skills.all %}}
                <div class="skill-item">
                    <div class="skill-name">{{{{ skill.name }}}}</div>
                    <div class="skill-level">{{{{ skill.proficiency }}}}</div>
                </div>
                {{% endfor %}}
            </div>
        </div>
        {{% endif %}}

        {'</div>' if layout == 'creative' else ''}

        <!-- Projects -->
        {{% if profile.projects.all %}}
        <div class="section">
            <h2 class="section-title">Projects</h2>
            {{% for project in profile.projects.all %}}
            <div class="project-item">
                <div class="item-header">
                    <div>
                        <div class="item-title">{{{{ project.name }}}}</div>
                        <div class="item-company">{{{{ project.technologies }}}}</div>
                    </div>
                    <div class="item-date">{{{{ project.start_date }}}} - {{{{ project.end_date }}}}</div>
                </div>
                <p>{{{{ project.description }}}}</p>
                {{% if project.url %}}
                <p><a href="{{{{ project.url }}}}" target="_blank" style="color: var(--primary-color);">View Project →</a></p>
                {{% endif %}}
            </div>
            {{% endfor %}}
        </div>
        {{% endif %}}
    </div>
</div>
{{% endblock %}}
"""
