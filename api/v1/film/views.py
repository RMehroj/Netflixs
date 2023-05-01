from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models, serializers


class ActorVievSet(ReadOnlyModelViewSet):
    queryset = models.Filmmakers.objects.all()
    serializer_class = serializers.FilmmakersSerializer


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializer
