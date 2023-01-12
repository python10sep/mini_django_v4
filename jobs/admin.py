from django.contrib import admin

# Register your models here.

##########################################################
# How to register models to django admin-interface?      #
##########################################################

from jobs.models import JobDescription, Applicant


admin.site.register(JobDescription)
admin.site.register(Applicant)

##########################################################