"""

django.views.generic
"""


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse

from django.urls import reverse_lazy

from jobs.models import Applicant, JobTitle, JobDescription, Portal


class ApplicantList(ListView):
    model = Applicant


class ApplicantCreate(CreateView):
    model = Applicant
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        breakpoint()
        return HttpResponse("<p>trial</p>")


class ApplicationUpdate(UpdateView):
    model = Applicant
    fields = ["id", "name", "cover_letter"]
    success_url = reverse_lazy("application_list")





