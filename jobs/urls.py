
from django.urls import path, re_path
from . import views  # import from current directory


urlpatterns = [
    re_path(r"^wel*", views.welcome),
    path("portal/", views.portal_details),
]