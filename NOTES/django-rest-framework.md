### STEPS

step 1: install DRF
```
pip install djangorestframework
```
step 2: update requirements.txt
step 3: update settings.py

```markdown
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
    'rest_framework'
]
```

step 4: create a class based view and based class it from `APIView` from drf.