## stateful application


- To maintain state of application django uses an application called `django.contrib.sessions`
- To persist state of application data under `request.session` is used.
- `request.session` is dict-like object

#### How to store objects in `request.session`?
- `request.session` is dict-like object
- `request.session["my_name"] = "prashant"`
- `request.session.modified = True` # To save session data

Alternatively, we can set following directive in `settings.py`
```
SESSION_SAVE_EVERY_REQUEST = True
```


## stateless application

- HTTP POST
- HTTP GET
- HTTP PUT

