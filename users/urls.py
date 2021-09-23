from django.urls import path, include
from .views import dashboard, register

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', register, name='register'),
    path('accounts/', include("django.contrib.auth.urls"))

]
