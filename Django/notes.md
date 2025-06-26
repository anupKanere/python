# Commands

- pip install Django
- django-admin startproject <project_name>
- cd <project_name>


# Request-Response Flow in Django

### Client (Browser/Frontend):

The process begins when a client (like a browser or any HTTP client) sends an HTTP request to the Django application.
WSGI Server:

The request is received by a WSGI (Web Server Gateway Interface) server like Gunicorn, uWSGI, or Django's development server.
The WSGI server forwards the request to Django for processing.
Django Middleware:

The request passes through the middleware layer. Middleware is a chain of hooks used to process requests and responses globally.

### Middleware can:
Modify the request object.
Add headers or authentication tokens.
Block invalid requests.

### URL Routing:

The request is then routed to the appropriate URL pattern defined in urls.py.
Django uses the URL dispatcher to match the requested URL to a specific view.


### View:

Once the correct URL pattern is matched, Django calls the corresponding view function or class-based view (CBV).
The view is where the business logic resides, such as:
- Fetching data from the database.
- Applying logic.
- Returning a response.
- Models:

If the view interacts with the database, it communicates with the models. Django's ORM (Object Relational Mapper) translates model queries into SQL statements and interacts with the database.
Templates:

If the view renders a template, it uses the Django Template Engine to combine data and HTML for the response.
Response:

The view function or CBV returns an HTTP response object. The response could be:
- HTML content.
- JSON or XML (for APIs).
- A file (e.g., PDF, CSV).

Middleware processes the response before it is sent back to the client.
Client Receives the Response:

The WSGI server sends the final response back to the client.

# Django Request-Response Flow

```plaintext
+-------------------+    HTTP Request     +-------------------+
|   Client (User)   | ------------------> |    WSGI Server    |
+-------------------+                     +-------------------+
                                                 |
                                                 v
                                  +-----------------------------+
                                  |       Django Middleware     |
                                  +-----------------------------+
                                                 |
                                                 v
                               +-------------------------------------+
                               |       URL Dispatcher/Resolver       |
                               +-------------------------------------+
                                                 |
                                                 v
                                  +-----------------------------+
                                  |            View             |
                                  +-----------------------------+
                                   /                            \
                                  v                              v
                      +------------------+          +------------------+
                      |      Models      |          |     Templates    |
                      +------------------+          +------------------+
                                   \                            /
                                    v                          v
                                  +-----------------------------+
                                  |      HTTP Response          |
                                  +-----------------------------+
                                                 |
                                                 v
                                    +---------------------+
                                    |     WSGI Server     |
                                    +---------------------+
                                                 |
                                                 v
                                   +---------------------+
                                   |       Client        |
                                   +---------------------+

```

### python manage.py startapp <app_name> - 
- Above command is used in Django to create a new application (app) within a Django project 
- ### What Happens: 
  When this command is run, Django generates a directory structure for the new app, which includes default files necessary for app development. For example, running python manage.py startapp blog creates a directory blog with the following structure:

```plaintext
blog/
    __init__.py       # Marks the directory as a Python package.
    admin.py          # File for registering models with the admin site.
    apps.py           # Configuration for the app.
    migrations/       # Directory for database migration files.
        __init__.py   # Marks the directory as a Python package.
    models.py         # File to define database models.
    tests.py          # File for writing unit tests.
    views.py          # File to define application logic.
```
- This command only creates the necessary files and folder structure for the app; however, the main project is not automatically aware of the new app. Additional below configuration is required to integrate the app with the main project.

- Add the app to the INSTALLED_APPS list in your project’s settings.py file: 
```
    INSTALLED_APPS = [
        ...,
        'blog',
    ]

```

## Notes :
- after creating the app it does not contains urls.py so we need to create that file inside our new app and then inform to main project that all the urls related to that project should pass throught that app so for that in main project urls.py we have to add one line to give control to main project for passing urls through sub urls.py files







