from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit_speaker/", views.submit_speaker, name="submit_speaker"),
    path("submit_registration/", views.submit_registration, name="submit_registration"),
    path("submit_sponsor/", views.submit_sponsor, name="submit_sponsor"),
    path("registration_count/", views.registration_count, name="registration_count"),
]
