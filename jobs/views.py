import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from jobs.models import Portal, JobTitle

# Create your views here.


def welcome(request):
    return HttpResponse("<p> welcome to this job board application</p>")


def get_portal_details(request):
    ##########################################################
    # How to get URL associated with django view?            #
    ##########################################################
    from django.urls import reverse

    print(reverse("details"))
    ##########################################################

    objs = Portal.objects.order_by("id")

    portals = []
    for obj in objs:
        portals.append(obj.name)

    final = "=====".join(portals)
    return HttpResponse(f"<p> {final} </p>")


def get_job_description(request, job_id):
    return HttpResponse(f"<p> {job_id} ::"
                        f" this job role requires candidate to have "
                        f"good understanding of django</p>")


def job_titles(request):
    """plural endpoint for getting all job titles"""

    job_titles_ = JobTitle.objects.all()

    response = {}
    for job in job_titles_:
        temp = dict()
        temp["job title"] = job.title
        temp["job descr"] = job.job_description.role
        response[job.id] = temp
    return JsonResponse(response)
