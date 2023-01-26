from django.views.decorators.csrf import csrf_exempt

from jobs.models import JobTitle, JobDescription
from jobs.serializers import JobTitleSerializer

from django.http import JsonResponse
from rest_framework.parsers import JSONParser


@csrf_exempt
def jobtitle_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        job_titiles = JobTitle.objects.all()
        serializer = JobTitleSerializer(job_titiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JobTitleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
