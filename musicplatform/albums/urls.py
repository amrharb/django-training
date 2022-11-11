from . import views
from django.urls import path
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('albums', views.AlbumViewSet)
songs_router = routers.NestedSimpleRouter(router, 'albums', lookup='album')
songs_router.register('songs', views.SongViewSet, basename='album-songs')

urlpatterns = [
    path('albums/filters/', views.ManualAlbumList.as_view()),
] + router.urls