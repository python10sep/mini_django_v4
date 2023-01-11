"""

## COMMAND

python manage.py shell

------------------------------------

from jobs.models import Portal

### TO INSERT NEW OBJECT IN DATABASE
Portal.objects.create(name="indeed.com", description="NEW")


-----------------------------------

# TO GET ALL THE OBJECTS
objs = Portal.objects.all()
for obj in objs:
    print(obj)
-----------------------------------

# TO FILTER PARTICULAR OBJECT BASED ON CERTAIN COLUMN
Portal.objects.get(name="naukri.com")

"""


from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.utils import timezone


class Portal(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name + "  " + self.description

    def launch(self):
        self.save()


class JobTitle(models.Model):
    title = models.CharField(max_length=250)
    last_updated = models.DateTimeField(default=timezone.now)
    portal = models.ForeignKey(Portal, on_delete=Portal)



