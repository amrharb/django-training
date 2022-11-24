from django.forms import ValidationError
from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer
from .filters import AlbumFilter
from .pagination import AlbumPagination
from .permissions import IsArtistPermission
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView


class AlbumViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtistPermission]
    queryset = Album.approved_album.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AlbumFilter
    pagination_class = AlbumPagination


class ManualAlbumList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsArtistPermission]
    serializer_class = AlbumSerializer
    pagination_class = AlbumPagination

    def get_queryset(self):
        queryset = Album.approved_album.all()
        name = self.request.query_params.get('name')
        cost_gte = self.request.query_params.get('cost__gte')
        cost_lte = self.request.query_params.get('cost__lte')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        try:
            if cost_gte is not None:
                queryset = queryset.filter(cost__gte=cost_gte)
            if cost_lte is not None:
                queryset = queryset.filter(cost__lte=cost_lte)
        except:
            raise ValidationError("cost can't be a string you should set it as an integer.")
        return queryset


class SongViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs['album_pk'])