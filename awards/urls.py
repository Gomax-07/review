from django.urls import path
from . import views
from .views import image_upload_view, HomePageView, display_project_images

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path('repo/', views.display_project_images, name='project_images'),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('upload/', views.image_upload_view),
    path('gallery/', HomePageView.as_view(), name='home'),
    path('search/', views.search_results, name='search_results'),
    path("gallery/<int:pk>/", views.image_detail, name="image_detail"),
    path("gallery/", views.image_index, name="image_index"),
]
