from django.contrib import admin
from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name','cost','approved']
    readonly_fields = ['created_at']