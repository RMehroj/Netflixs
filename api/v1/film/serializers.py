from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import datetime
from .models import Position, Filmmakers, Movies, Comment
from netflix.serializers import  DynamicFieldsModelSerializer


class PositionSerializers(DynamicFieldsModelSerializer):

    class Meta:
        model = Position
        fields = [
            'position',
        ]


class FilmmakersSerializer(DynamicFieldsModelSerializer):
    positions = PositionSerializers(
        read_only=True, 
        fields = ["position"],
    )

    class Meta:
        model = Filmmakers
        fields = [
            'name',
            'age',
            'gender',
            'positions',
        ]


class MoviesSerializer(DynamicFieldsModelSerializer):
    filmmakers = FilmmakersSerializer(many=True)

    class Meta:
        model = Movies
        fields = [
            'title',
            'production_year',
            'imdb',
            'genre',
            'filmmakers',
        ]


class CommentSerializer(DynamicFieldsModelSerializer):
    # user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            'movie_id', 
            'user_id', 
            'text', 
            'created_date',
        ]