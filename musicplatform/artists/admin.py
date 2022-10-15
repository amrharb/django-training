from django.contrib import admin
from .models import Artist
from albums.models import Album
from django.utils.html import format_html


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display= ['Stage_name','SocialLink','approved_albums']
    list_per_page = 10
    inlines = [
        AlbumInline,
    ]

    def SocialLink(self, artist):
        return format_html('<a href={}>{}</a>', artist.Social_link, artist.Social_link)

    def approved_albums(self, artist):
        cnt = 0
        for album in artist.albums.all():
            if album.approved == 1:
                cnt += 1

        return cnt
