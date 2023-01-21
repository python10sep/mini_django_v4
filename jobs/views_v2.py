from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from jobs.models import Portal, JobTitle, Applicant, JobDescription


class ApplicantList(ListView):
    model = Applicant


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["name", "cover_letter"]
    success_url = reverse_lazy("applicant_list")


class ApplicantDelete(DeleteView):
    model = Applicant
    success_url = reverse_lazy("applicant_list")
