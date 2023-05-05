from django.urls import path, include
from rest_framework.authtoken import views



urlpatterns = [
    path(
        "register/",
        views.UserRegistrationView.as_view(),
        name="register",
    ),
]