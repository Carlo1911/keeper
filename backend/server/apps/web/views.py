from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import WebBookmark
from .serializers import WebBookmarkSerializer


@extend_schema_view(
    list=extend_schema(
        summary='List all Web Bookmarks',
        description='Return a list of all web bookmarks in the system.',
        tags=['Web Bookmarks'],
    ),
    retrieve=extend_schema(
        summary='Retrieve a Web Bookmark',
        description='Get details of a specific web bookmark',
        tags=['Web Bookmarks'],
    ),
    create=extend_schema(
        summary='Create a Web Bookmark',
        description='Create a web bookmark',
        tags=['Web Bookmarks'],
    ),
    update=extend_schema(
        summary='Update a Web Bookmark',
        description='Update details of a specific web bookmark',
        tags=['Web Bookmarks'],
    ),
    partial_update=extend_schema(
        summary='Partial update a Web Bookmark',
        description='Update details of a specific web bookmark',
        tags=['Web Bookmarks'],
    ),
    destroy=extend_schema(
        summary='Delete a Web Bookmark',
        description='Delete a specific web bookmark',
        tags=['Web Bookmarks'],
    ),
)
class WebBookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = (
        WebBookmark.objects.filter(public=True).select_related('user').order_by('id')
    )
    serializer_class = WebBookmarkSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user and self.request.user.is_authenticated:
            queryset = qs | WebBookmark.objects.filter(
                public=False, user=self.request.user
            ).select_related('user').order_by('id')
            return queryset.distinct()
        return qs
