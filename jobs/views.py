import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from jobs.models import Portal, JobTitle, JobDescription

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
    return HttpResponse(f"<h1> {final} </h1>")


def get_job_description(request, job_id):
    jd = JobDescription.objects.get(pk=job_id)
    return render(request, "jobs/job_description.html", {"job_desc": jd})

    ############################################################
    # # How to send HttpResponse Object from request           #
    # ##########################################################
    # return HttpResponse(f"<p> {job_id} ::"
    #                     f" this job role requires candidate to have "
    #                     f"good understanding of django</p>")
    ############################################################


def job_titles(request):
    """plural endpoint for getting all job titles"""

    job_titles_ = JobTitle.objects.all()
    return render(
        request,
        "jobs/job_titles.html",
        {"objects": job_titles_}
    )

    # ##########################################################
    # # How to send JsonResponse Object from request           #
    # ##########################################################
    #
    # response = {}
    # for job in job_titles_:
    #     temp = dict()
    #     temp["job title"] = job.title
    #     temp["job descr"] = job.job_description.role
    #     response[job.id] = temp
    # return JsonResponse(response)
    # ############################################################
