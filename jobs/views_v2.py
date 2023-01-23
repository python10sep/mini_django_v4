from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from jobs.models import Applicant, JobTitle, JobDescription, Portal


class ApplicantList(ListView):
    model = Applicant
    template_name = "jobs/applicant_list1.html"






