
from django.urls import path, re_path
from . import views  # import from current directory


urlpatterns = [
    re_path(r"^wel*", views.welcome, name="welcome"),
    path("portal/", views.portal_details, name="details"),
    path("<int:job_id>/", views.job_description, name="JD")
]
##########################################################
# How to capture PATH parameters from URL?               #
##########################################################
# Notes:
#
# To capture a value from the URL, use angle brackets.
# Captured values can optionally include a converter type.
# For example, use <int:name> to capture an integer parameter.
# If a converter isn’t included,
# any string, excluding a / character, is matched.
# There’s no need to add a leading slash, because every URL has that.
# For example, it’s articles, not /articles.

##########################################################

