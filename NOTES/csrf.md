## SAFE METHODS
- GET  (read-only)


## UNSAFE METHODS
- POST, DELETE, PUT, PATCH

Server  <----->  client (postman, browser)


## phishing attack

facebook.com login 


## CSRF (Cross Site Request Forgery) attack

## Middleware
-  middleware is a class that comes in between request and response cycle
- `django.middleware.csrf.CsrfViewMiddleware` disallows POST, PUT, DELETE and PATCH request.

## How to skip CSRF?
- either comment out middleware
- OR use decorator `csrf_exempt`
- `from django.views.decorators.csrf import csrf_exempt`
