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

    def delete_model(self, request, Song):
        if Song.album.songs.count()>1:
            Song.delete()
        else:
            self.message_user(request, 
                "you can't delete all songs of an album",
                messages.ERROR
              )  
              
    def delete_queryset(self, request, queryset):
        has_error = False
        for song in queryset:
            album = song.album 
            if album.songs.count()>1:
                song.delete()
            else :
                has_error = True

        if has_error:
              self.message_user(request, 
                "you can't delete all songs of an album",
                messages.ERROR
              )  
