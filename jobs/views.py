import logging
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from jobs.models import Portal, JobTitle, JobDescription
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def welcome(request):

    # number of times user has visited web page
    user_pk = request.session.get("_auth_user_id")
    user = User.objects.get(pk=int(user_pk)) if user_pk else ""
    username = user.username if user else "Unknown user"

    visits = request.session.get("user_visits", 0)
    request.session["user_visits"] = visits + 1
    request.session.modified = True
    response = HttpResponse(f"<p> welcome to this job board application -{username} visits {visits} times ()</p>")
    return response


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

    return JsonResponse(portals, safe=False)


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


@csrf_exempt
def job_titles(request):
    """plural endpoint for getting all job titles"""

    if request.method == "POST":
        data = json.loads(request.body)

        # TODO: perform a check if certain job_title already exist
        # TODO: if title exists, return a message.

        # portal
        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**portal_data)
            portal.save()
        else:
            portal = portal[0]

        jd = data.get("job_description")
        jd = JobDescription.objects.create(**jd)
        jd.save()
        data["job_description"] = jd
        data["portal"] = portal
        jt = JobTitle.objects.create(**data)
        jt.save()

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


    # ##########################################################
    # # How to write a POST request endpoint in django?        #
    # ##########################################################



