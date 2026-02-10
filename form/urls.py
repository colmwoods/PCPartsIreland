from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("success/", views.success, name="success"),
    path("returns/", views.return_request, name="return_request"),
    path("returns/success/", views.return_success, name="return_success"),
]