```
Author		- SMASTERRK
Designation	- FullStackDeveloper
```


# Install Django and Django REST framework 
--pip install django
--pip install djangorestframework

# Set up a new project with a single application
--django-admin startproject pythonRest
--cd pythonRest
--django-admin startapp quickstart

#Now sync your database for the first time:
--python manage.py migrate
--python manage.py createsuperuser --email admin@example.com --username admin


#Complete your application and required changes in views, urls, settings file

#Test your API
--python manage.py runserver


#If you created with your custom Models for your Python Rest Application
#Then before starting do the following, and then execute the commands given before starting the application

>>Delete your database (db.sqlite3 in my case) in your project directory
>>Remove everything from __pycache__ folder under your project subdirectory

--python manage.py makemigrations
--python manage.py migrate











