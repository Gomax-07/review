from django.contrib import admin

# Register your models here.
from .models import Author, Technology, Project, Detail, Image

admin.site.register(Project)
admin.site.register(Author)
admin.site.register(Technology)
admin.site.register(Detail)
admin.site.register(Image)

