from django.urls import path
from . import views


urlpatterns = [
    path("",views.ArtistsView.as_view()),
]