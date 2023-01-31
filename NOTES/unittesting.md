## in-built `unittest` module

- We write test cases by base-classing from `unittest.TestCase`
- Any instance method under that class has to be prefixed with `test_` (if its a test case)
- assert statements (https://docs.python.org/3/library/unittest.html#assert-methods)
- 

## Django Test Framework

- Created on top of `unittest` library
- Django test framework has following features -
  - Test Client - dummy browser
  - Simulate browser actions (GET, PUT, POST,... etc)
  - Temporary DB
  
## How do we write test cases in Django?
- `django-admin startapp <application>` this command produces certain files
- We can either use file called `tests.py` auto-created by django under application
- OR, we have to delete `tests.py` under app and create a package called `tests`
- Any test file created under `tests` package has to be prefixed with `test_`
- Any instance method created under test class  has to be prefixed with `test_`
- Test classes need to be based classed from `django.test.TestCase`

## How to run django test suite?
- `python manage.py test`

## what is `test fixures`?
- In order perform test, we need some setup.
- 
```python
    def setUp(self) -> None:
        self.obj = Portal.objects.create(
            name="jobsportal2.in",
            description="new portal in market"
        )

```

## what is `teardown`?
- after we perform test, we need to destroy setup.
```python
    def tearDown(self) -> None:
        Portal.delete(self.obj)
```