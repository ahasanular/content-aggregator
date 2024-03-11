from django.urls import path

from .views import favorites_template, FavoriteAPIView, AddToFavoritesView


urlpatterns = [
    path("", favorites_template, name="favorites"),
    path(
        'add_to_favorites/<pk>/',
        AddToFavoritesView.as_view(),
        name='add_to_favorites'
    ),
    path(
        'api/favorites/',
        FavoriteAPIView.as_view(),
        name='favorite_list_api'

    )
]
