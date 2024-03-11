from django.urls import path

from .views import ExploreAPIView, explore_page


urlpatterns = [
    path("", explore_page, name="explore"),
    path("api/explore/", ExploreAPIView.as_view(), name="explore_api"),
]
