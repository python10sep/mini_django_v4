import logging
from django.shortcuts import render
from django.http import HttpResponse
from jobs.models import Portal

# Create your views here.


def welcome(request):
    return HttpResponse("<p> welcome to this job board application</p>")


def portal_details(request):
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


def job_description(request, job_id):
    return HttpResponse(f"<p> {job_id} ::"
                        f" this job role requires candidate to have "
                        f"good understanding of django</p>")
