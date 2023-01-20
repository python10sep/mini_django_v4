from django.contrib import admin

# Register your models here.

##########################################################
# How to register models to django admin-interface?      #
##########################################################

from jobs.models import JobDescription, Applicant, Portal, JobTitle


admin.site.register(JobDescription)
admin.site.register(Applicant)
admin.site.register(Portal)
admin.site.register(JobTitle)

############################################################
