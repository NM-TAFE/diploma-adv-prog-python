
**Start a New Project**  
Create a new Django project structure.
```bash
django-admin startproject project_name
```

**Start a New App**  
Create an app within a project.
```bash
python manage.py startapp app_name
```

**Run Development Server**  
Start the local server for testing.
```bash
python manage.py runserver
```

**Create Migrations**  
Generate migration files for model changes.
```bash
python manage.py makemigrations
```

**Apply Migrations**  
Update the database schema.
```bash
python manage.py migrate
```

**Undo/Rollback Migrations**  
Go back to a specific migration.
```bash
python manage.py migrate notifier 0002
```

**Create Superuser**  
Set up an admin user for the Django admin dashboard.
```bash
python manage.py createsuperuser
```

**Collect Static Files**  
Gather static files for production (js, css, img etc...).
```bash
python manage.py collectstatic
```

**Run Tests**  
Run the project’s tests.
```bash
python manage.py test
```

## ORM Queries
**Retrieve All Objects**  
Fetch all instances of a model.
```python
Model.objects.all()
```

**Filter Objects**  
Query objects matching specific criteria.
```python
Model.objects.filter(field_name="value")
```

**Get a Single Object**  
Retrieve one object or raise an exception.
```python
Model.objects.get(field_name="value")
```

**Create an Object**  
Save a new instance to the database.
```python
Model.objects.create(field_name="value")
```

**Update Objects**  
Modify existing objects in bulk.
```python
Model.objects.filter(field_name="value").update(new_field="new_value")
```

**Delete Objects**  
Remove objects from the database.
```python
Model.objects.filter(field_name="value").delete()
```

**Optimised Queries**  
Use `select_related` for foreign keys & `prefetch_related` for many-to-many relationships.
```python
Model.objects.select_related('foreign_key').all()
Model.objects.prefetch_related('many_to_many_field').all()
```

**Aggregate Data**  
Get model meta like count or sum.
```python
from django.db.models import Count
Model.objects.aggregate(Count('field_name'))
```

## Template Tags

Django’s template system uses tags and filters for dynamic rendering.

### Load Static Files
Include CSS, JavaScript, or images.
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

### Loop Over Data
Iterate over a queryset or list.
```html
{% for item in items %}
  <p>{{ item.field_name }}</p>
{% empty %}
  <p>No items found.</p>
{% endfor %}
```

### Conditional Rendering
Display content based on conditions.
```html
{% if user.is_authenticated %}
  <p>Welcome, {{ user.username }}!</p>
{% else %}
  <p><a href="{% url 'login' %}">Login</a></p>
{% endif %}
```

### URL Resolution
Generate URLs for named routes.
```html
<a href="{% url 'view_dashboard' user_id%}">Link</a>

<!-- This renders -->
<a href="/dashboard/1/">Article Title</a>
```

### Include Templates
Reuse templates.
```html
{% include 'confidence.html' %}
```

### Extend Templates
Use template inheritance for shared layouts.
```html
{% extends 'base.html' %}
{% block content %}
  <!-- Child content -->
{% endblock %}
```

### Format Data
Apply filters to format variables.
```html
{{ date_field|date:"F d, Y" }}
{{ text|truncatewords:30 }}
```
