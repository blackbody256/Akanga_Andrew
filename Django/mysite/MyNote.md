# Django Notes:
### File Directories:
- **Project Directory**: Contains the `manage.py` file and the main project folder.
- **manage.py**: A command-line utility for administrative tasks.
    - Purpose: Command-line utility that lets you interact with the Django project.
    - Usage: Run server, create apps, run migrations, create superuser, etc.
    - Never modify this file, it's automatically generated.
    **Example Commands**:
    ```shell
    python manage.py runserver  # Start the development server
    python manage.py makemigrations  # Create new migrations based on changes
    python manage.py migrate  # Apply migrations to the database
    python manage.py createsuperuser  # Create a superuser for the admin interface
    python manage.py collectstatic  # Collect static files for deployment
    python manage.py shell  # Open a Python shell with Django context
    python manage.py test  # Run tests for the project
    python manage.py startapp appname  # Create a new Django app called appname
    python manage.py check  # Check the project for any issues
    python manage.py dumpdata appname.ModelName  # Export data from a model to JSON
    python manage.py loaddata appname.ModelName  # Load data from JSON into a model
    python manage.py flush  # Reset the database (use with caution)
    ```
- **Apps Directory**: Contains individual Django apps.
- **Project Folder**: Contains settings, URLs, and WSGI files.
- **__init__.py**: Marks the directory as a python package.
    - Purpose: Empty file that tells python this director is a package.
    - Usage: rarely modified, but can be used to define package-level variables or imports.
- **settings.py**: Contains project settings and configuration.
    - Key sections:
        - Database configuration: Defines the database connection settings.
        - Installed apps: Lists all Django apps included in the project.
        - Middleware: Defines middleware components that process requests and responses.
        - Static files: Configuration for serving static files.
        - Templates: Configuration for template engines.
        - Logging: Configuration for logging messages.
        - Security settings: Defines security-related configurations like allowed hosts, CSRF, and session settings.
- **urls.py**: Maps URLs to views like web.php in Laravel.
- **WSGI.py**: WSGI entry point for deployment.
    - Deploying to production servers like Apache or Nginx.
    - Rarely modified, but can be used to define WSGI application callable.
- **asgi.py**: ASGI entry point for asynchronous deployment.
    - Asynchronous applications, websockets, real-time features.

### Django projects VS Django apps:
- **Django Project**: A collection of settings and configurations for a specific site.
- **Django App**: A web application that does something, e.g., a blog, a database of public records, or a survey application.
    - A project can contain multiple apps.
    - An app can be reused in multiple projects.

#### Django App Structure:
- __init__.py: Marks the directory as a Python package.
- admin.py: Configuration for the Django admin interface.
- apps.py: Configuration for the app itself.
- models.py: Defines the data models (database schema).
- tests.py: Contains tests for the app.
- views.py: Contains the logic for handling requests and returning responses. Just like controllers in Laravel.
- migrations/: Directory for database migrations.
- static/: Directory for static files (CSS, JavaScript, images).
- templates/: Directory for HTML templates.
- urls.py: Maps URLs to views within the app.