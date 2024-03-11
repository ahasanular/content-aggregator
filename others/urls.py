from django.urls import path

from .views import AboutUsView, ContactUsView, ContactUsSuccessView


urlpatterns = [
    path("about/", AboutUsView.as_view(), name="about"),
    path("contact/", ContactUsView.as_view(), name="contact_us"),
    path(
        'contact/success/',
        ContactUsSuccessView.as_view(),
        name='contact_us_success'
    ),
]
