from django.contrib import admin

from . import models

@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Filmmakers)
class FilmmakersAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Movies)
class MoviesAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
