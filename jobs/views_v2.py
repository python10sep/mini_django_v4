"""

django.views.generic
"""


from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from jobs.models import Applicant, JobTitle, JobDescription, Portal


class ApplicantList(ListView):
    model = Applicant


class ApplicationUpdate(UpdateView):
    model = Applicant
    fields = ["name", "cover_letter"]
    success_url = reverse_lazy("application_list")





