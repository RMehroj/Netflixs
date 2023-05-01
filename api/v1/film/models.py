from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

from netflix.models import BaseModel


class Position(BaseModel):
    
    position = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'Position'

    def __str__(self):
        return self.position


class Filmmakers(BaseModel):

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'),
                      (GENDER_FEMALE, 'Female')]

    name = models.CharField(max_length=150, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    positions = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Filmmakers'

    def __str__(self):
        return self.name
    

class Movies(BaseModel):

    GENRE_COMEDY = 0
    GENRE_ROMANTIC = 1
    GENRE_THRILLER = 2
    GENRE_HORROR = 3
    GENRE_CHOICES = [(GENRE_COMEDY, 'Comedy'),
                 (GENRE_ROMANTIC, 'Romantic'),
                 (GENRE_THRILLER, 'Thriller'),
                 (GENRE_HORROR, 'Horror')]

    title = models.CharField(max_length=256, blank=False, null=False)
    production_year = models.DateField(auto_now=True, blank=True)
    imdb = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    genre = models.IntegerField(choices=GENRE_CHOICES, blank=False, null=False)
    filmmakers = models.ManyToManyField(Filmmakers)

    class Meta:
        db_table = 'Movie'

    def __str__(self):
        return self.title


User = get_user_model()

class Comment(BaseModel):
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=512)
    created_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'Comment'

    def __str__(self):
        return self.text
