from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preview/<int:pk>/', views.preview, name='preview'),
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('edit/<int:pk>/', views.edit_resume, name='edit_resume'),
    path('gallery/', views.template_gallery, name='template_gallery'),
]
