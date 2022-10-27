from django.contrib import admin,messages
from .models import *

class SongInline(admin.TabularInline):
    model = Song
    extra = 0
    min_num = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]
    list_display = ['name','cost','approved']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    readonly_fields = ('image_thumbnail',)
    class Meta:
        fields='__all__'

    def delete_queryset(self, request, queryset):
        albums_counter = {}
        has_error = False
        for song in queryset:
            album = song.album 
            if not album.id in albums_counter:
                albums_counter[album.id] = album.songs.count()
            
            if albums_counter[album.id]>1:
                song.delete()
                albums_counter[album.id]-=1
            else :
                has_error = True

        if has_error:
              self.message_user(request, 
                "you can't delete all songs of an album",
                messages.ERROR
              )    