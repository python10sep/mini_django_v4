
# how does django process request?

- Django middleware is a class/ function that comes in between HTTP request and response
- For example, django has built-in session middleware `django.contrib.sessions.middleware.SessionMiddleware`
- It adds data to the `request.session` object
- django middlewares play before view and after view