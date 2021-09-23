from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from awards import views
from awards.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("awards.urls")),
    path('', include('users.urls')),


    path("image/", views.home_view, name="home_view"),
    path('image_upload/', project_image_view, name='image_upload'),
    path('success', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
