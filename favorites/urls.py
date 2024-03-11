from django.urls import path

from .views import FavoritesView, UpdateFavoriteView


urlpatterns = [
    path("", FavoritesView.as_view(), name="favorites"),
    path('update_favorite/<int:episode_id>/', UpdateFavoriteView.as_view(), name='update_favorite'),
]
