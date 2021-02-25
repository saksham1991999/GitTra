from django.contrib import admin

from .models import Repository

admin.site.site_header = "GitTra"

admin.site.register(Repository)