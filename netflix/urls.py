
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'api/v1/admin/',
        admin.site.urls),

    path(
        "", 
        include('api.v1.film.urls')),
]
