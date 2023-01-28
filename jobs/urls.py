"""
NOTE - URLS we have

http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/jobs/portal/
http://127.0.0.1:8000/jobs/jobtitles/
http://127.0.0.1:8000/jobs/<job_id>/



http://127.0.0.1:8000/jobs/jobtitles  (PLURAL endpoint)
http://127.0.0.1:8000/jobs/jobtitles/1/ (SINGULAR endpoint)

"""

from django.urls import path, re_path
from . import views  # import from current directory (function based views)
from . import views_v2  # (class based views)
from . import views_v3  # (class based view - using django rest framework )
from . import views_v4 # (function based view - using DRF and DRF-serialier)



urlpatterns = [
    re_path(r"^wel*", views.welcome, name="welcome"),
    path("portal/", views.get_portal_details, name="details"),
    path("jobtitles/", views.job_titles, name="jobtitle"),
    path("jobtitles/<int:job_id>/", views.get_job_description, name="JD"),

    ## v2 URLs (created for generic class based views)
    path(
        "v2/applicants/",
        views_v2.ApplicantList.as_view(),
        name="v2_applicant_list"
    ),
    path(
        "v2/applicants/create",
        views_v2.ApplicantCreate.as_view(),
        name="v2_applicant_create"
    ),
    path(
        "v2/applicants/update/<int:pk>",
        views_v2.ApplicantUpdate.as_view(),
        name="v2_applicant_update"
    ),

    ## v3 URLs (created for django rest framework APIView)
    path(
        "v3/applicants/",
        views_v3.Applicants.as_view(),
        name="v3_applicant_list"
    ),
    path(
        "v3/users/",
        views_v3.UserList.as_view(),
        name="v3_users_list"
    ),

    ## v4 URLs (created using DRF and Django Rest Framework)
    path(
        "v4/jobtitles",
        views_v4.jobtitle_list,
        name="v4_jobtitles_list"
    )
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

