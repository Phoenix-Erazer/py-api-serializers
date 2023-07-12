from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema-halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie-session", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
