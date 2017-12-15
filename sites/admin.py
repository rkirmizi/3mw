from django.contrib import admin
from .models import Site, SiteDetail

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteDetail)
class SiteDetailAdmin(admin.ModelAdmin):
    pass