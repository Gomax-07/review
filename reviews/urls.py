from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from projects import views
from projects.views import success

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("projects.urls")),
    path("image/", views.home_view, name="home_view"),
    path('success', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
