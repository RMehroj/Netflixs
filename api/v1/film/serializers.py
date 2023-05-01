from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import datetime
from film.models import Position, Filmmakers, Movies, Comment

class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = [
            'position',
            ]


class FilmmakersSerializer(serializers.ModelSerializer):
    positions = PositionSerializers(
        read_only=True,
        fields=["positions"],
    )
    class Meta:
        model = Filmmakers
        fields = [
            'name',
            'age',
            'gender',
            'positions',
            ]


class MoviesSerializer(serializers.ModelSerializer):
    filmmakers = FilmmakersSerializer(many=True)

    class Meta:
        model = Movies
        fields = [
            'id',
            'name',
            'year',
            'imdb',
            'genre',
            'filmmakers',
        ]


class CommentSerializer(serializers.ModelSerializer):
    # user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = [
            'movie_id', 
            'user_id', 
            'text', 
            'created_date',
            ]