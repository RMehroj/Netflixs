from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from django.contrib.postgres.search import TrigramSimilarity

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from . import models, serializers


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['title', 'genre', 'production_year',]

    def get_queryset(self):
        queryset = models.Movies.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset =queryset.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.3).order_by('-similarity')
        return queryset


class ActorVievSet(ReadOnlyModelViewSet):
    queryset = models.Filmmakers.objects.all()
    serializer_class = serializers.FilmmakersSerializer