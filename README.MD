## Introduction
Cloud Platform Programing Project is a simple application developed using Django and Python that performs basic CRUD operation (to create/read/update and delete recipes). SQLite is used for persisting data. 

### Run Server
`python3 manage.py runserver 8080`
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 28, 2023 - 09:55:07
Django version 3.1.7, using settings 'foodanic.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.

```

## Navigating the Application
Post a new recipe
View the list of recipe and check the details of each recipe 
Edit the recipe 
Delete the recipe 

### Create Django Admin User
`python manage.py createsuperuser`
```
Username : admin
Email address: admin@project.com
Password: 
Password (again): 
Superuser created successfully.
```
### Reset Password
`python manage.py changepassword <user_name>`
```
Changing password for user 'admin'
Password: 
Password (again): 
Password changed successfully for user 'admin'
```

### Deploying on ELastic beanstalk 
install awsebcli : 
$ pip install awsebcli --upgrade --user

Install requirements.txt to see what packages are required for EC2 instance 
$ pip freeze > requirements.txt

create a directory 
 $ mkdir .ebextensions

create a file django.congif 
 $ touch .ebextensions/django.config
 
save the settings in django.config 
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: foodanic.wsgi:application
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: static/
    /media: media/
    
 Deactivate the environment 
  $ deactivate
  
  Create an environment in elastic beanstalk 
  $ eb init -r us-west-1 -p python-version applicationname
 
 

