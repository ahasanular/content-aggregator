from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import login_page, register_page, CustomRegisterView


urlpatterns = [
    path("login/", login_page, name="login"),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/register/',
        CustomRegisterView.as_view(),
        name='register_api'
    ),
    path(
        'register/',
        register_page,
        name='register'
    ),
]
