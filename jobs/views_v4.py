import json
from jobs.models import JobTitle
from jobs.serializer import JobTitleSerializer, JobDescriptionSerializer, PortalSerializer
from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# @csrf_exempt
def jobtitle_list(request):

    if request.method == "GET":
        job_titles = JobTitle.objects.all()
        serializer = JobTitleSerializer(job_titles, many=True)

        # ## Alternatively,
        # response = json.loads(json.dumps(serializer.data))
        # return JsonResponse(response, safe=False)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        parser = JSONParser()
        data = parser.parse(request)

        # job desc related
        jd_data = data.get("job_description")
        jd_data_serializer = JobDescriptionSerializer(data=jd_data)
        if jd_data_serializer.is_valid():
            jd_data_serializer.save()

        # portal related
        portal_data = data.get("portal")
        portal_serializer = PortalSerializer(data=portal_data)
        if portal_serializer.is_valid():
            portal_serializer.save()

        data["job_description"] = jd_data_serializer
        data["portal"] = portal_serializer

        serializer = JobTitleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        response = {
            "title": serializer.data.get("title"),
            "jd": jd_data_serializer.data.get("role"),
            "portal": portal_serializer.data.get("name")
        }

        return JsonResponse(response)





