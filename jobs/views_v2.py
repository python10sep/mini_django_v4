"""
This module demonstrates how to implement Django generic views.

Step 1 : create a BaseView using `django.views.generic.View`
"""


from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from jobs.models import Applicant, JobTitle, JobDescription, Portal


class ApplicantList(ListView):
    model = Applicant


class ApplicantCreate(CreateView):
    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("v2_applicant_list")


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["id", "name"]
    success_url = reverse_lazy("v2_applicant_list")





