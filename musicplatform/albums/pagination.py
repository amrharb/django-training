from rest_framework import pagination


class AlbumPagination(pagination.LimitOffsetPagination):
    default_limit = 1