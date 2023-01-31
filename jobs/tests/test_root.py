"""

# test_root.py

http://127.0.0.1:8000/jobs/welcome
http://127.0.0.1:8000/jobs/portal/
http://127.0.0.1:8000/jobs/jobtitles/
http://127.0.0.1:8000/jobs/jobtitles/1

# v2 URLs

# test_v2.py

http://127.0.0.1:8000/jobs/v2/applicants/
http://127.0.0.1:8000/jobs/v2/applicants/update/1

"""


from django.test import TestCase
from rest_framework.test import APIClient
from jobs.models import Portal


class RootTests(TestCase):
    """ Test getting greetings """

    def setUp(self) -> None:
        self.obj = Portal.objects.create(
            name="jobsportal2.in",
            description="new portal in market"
        )

    def tearDown(self) -> None:
        Portal.delete(self.obj)

    def test_welcome(self):

        client = APIClient()

        res = client.get("/jobs/welcome")
        self.assertEqual(res.status_code, 200)

    def test_portal(self) -> None:
        client = APIClient()
        res = client.get("/jobs/portal/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("jobsportal2.in", res.json())




