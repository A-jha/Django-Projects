## What is Django?

- A Python Web Framework
- Free and Open source
- Encourages Rapid Devllopment
- It is scallable

### Companies

- Sentry -- error logging project
- udemy
- Instagram
- Open EDX

## Installation

step1:

```python
 Install Python
```

step2: Install PIP

```pyhon
 sudo apt install python3-pip
```

step3: install django

```bash
 pip install django
 sudo apt install python3-django
```

step4: start project

```bash
 djago-admin startproject djcrm
```

step5:change directory

```bash
 cd djcrem
```

step6: Run server

```bash
python3 mange.py runserver
```

## walking thorough file of our project

- asgi.py --ASGI (Asynchronous Server Gateway Interface) is a spiritual successor
  to WSGI, intended to provide a standard interface between async-capable
  Python web servers,frameworks, and applications.

      Django also supports deploying on ASGI,

  the emerging Python standard for asynchronous web servers and applications.

- wsgi.py -- Where WSGI provided a standard for synchronous Python apps,
  ASGI provides one for both asynchronous and synchronous apps,
  with a WSGI backwards-compatibility implementation
  and multiple servers and application frameworks.

      WSGI is the Web Server Gateway Interface.

  It is a specification that describes how a web server
  communicates with web applications, and how web applications can be chained
  together to process one request.

- setting.py -- A Django settings file contains all the configuration
  of your Django installation.

## About my apps

CRM stands for “Customer Relationship Management” and refers to all strategies,
techniques, tools, and technologies used by enterprises for developing,
retaining and acquiring customers.
Apps are used to containarize the logic of our project.
crm is all about leads so create an app leads

### creating App Leads

```bash
python3 manage.py startapp leads
```

- migration folder -`__init__.py` will show the changes in database
  `__init__.py` - basically making leads a module
- `admin.py` - this will deals with django admin
- `app.py` -- configure leads folder as an app
- `models.py` - to creates model on databases
- `test.py` - for testing purpose
- `views.py` - used to handle web request and responses

## Register The app

inorder to register the app by django we need to go to
`settings.py`

```python
INSTALLED_APPS['leads',]
```

## leads/models.py

- Basically models are a representation of your database schema.
- each model maps to a single database table.
- We will create a class say lead and this class will inherit from models.
- Model
  (.Model is a python class inside models)

```python
class Lead(models.Model):
#field
first_name = models.CharField(max_length=20)

last_name = models.CharField(max_length=20)

age = models.IntegerField(default=0)
```

basically this will create a schema

```bash
python3 manage.py makemigrations
```

according to this model that we created. it will create a file in migration
folder with name `0001_initial.py` .

```python
python3 manage.py migrate
```

Django is goin to look through all the migration's
file and solidify the chages made or applly the changes.

**_Django sets Primeary key by default_ .**

### Foreign key

```python
class Lead(models.Model):
            SOURCE_CHOICE = (
                 ('google','google'),
                 ('youtube','youtube'),
                 ('website','website'),)
    phoned = models.BooleanField(default=False)
#source = models.CharField(choices=(
# ('google','google'),
# ('youtube','yt'), #
# ('website','website'),))
    source = models.CharField(choices=SOURCE_CHOICE,max_length=100) # profle_picture = models.ImageField(blank=True,null=True) # special_file = models.FileField(blank=True,null=True)
#field
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
#CASCADE - if agent gets deleted then leads will be deleted
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)
```

```python
#SET_NULL - if agent gets deleted then set agent of lead as null
#inthis case we have to allow null value true
agent = models.ForeignKey("Agent",on_delete=models.SET_NULL,null=True)
```

```python
#SET_DEFAULT - It will allow us to set a defult value # and we have to set adefult value too
agent = models.ForeignKey("Agent",on_delete=models.SET_DEFAULT,default=0)
```

- `"Agent"` - **double quotes signifies that Agents is present in `models.py`
  file but defined below the leads.**

```python
class Agent(models.Model):
first_name = models.CharField(max_length=20)
last_name = models.CharField(max_length=20)
```

- Basically agent is set to be the foreign key of lead because an Agent can have
- multiple leads but each Ajent must have only one Agent.

**learn about from django.contrib.auth.models import AbstractUser**

### Model Manager

it will lead you to the inegrated shell

```shell
python3 manage.py shell
```

- A car model which contains
  - make with choices
    - CAR_MANUFACTURERS
  * model
  * year

```python
class Car(models.Model):
CAR_MANUFACTURERS = (
('Audi','Audi'),
('BMW','BMW'),
('Ferrari','Ferrari'),
)
make = models.CharField(max_length=20,choices=CAR_MANUFACTURERS)
model = models.CharField(max_length=20)
year = models.ImageField(default=2015)
```

- to access the model manager, we use:

```python
Car.objects
```

it is calling the model manager on the manager
we have access to bunch of methods which allows us to query with the database and
perform action

- Using the manager we can create new cars:

```python
Car.objects.create(make="BMW",model = "X5",year=2017)
```

- query all cars in the database

```python
Car.objects.all()
```

- query for car with make equal to "Audi"

```python
Car.objects.filter(make="Audi")
```

- query for car with year greater than 2016

```python
Car.objects.filter(year__gt=2016)
```

## Register your model

step1: go to `admin.py` file<br>
step2:

```python
from .models import <your mdels>
```

step3:

```python
admin.site.register(<one model name>)
```

#### Example

```python
from django.contrib import admin

# Register your models here.
from .models import  User

admin.site.register(User)
```

## How to add templates into django project

#### First Method :

- Create a folder inside app named as templates

- Than create another folder named as the name of the app
- App
  - templates
    - App
- Than you can access the html file on views

```python
return render(req,"leads/home_page.html")
```

#### Second Method :

- Adding a folder with name templates in root directory

- Create a folder in root directory by name templates
- than go to `settings.py` and in TEMPLATES

```python
'DIRS': [BASE_DIR / "templates"],
```

- than we can add directly the teplates to `views.py` <b>without specifing the path.</b>

```python
return render(req,"secondpage.html")
```

## Views

- view function, or view for short, is a Python function
  that takes a Web request and returns a Web response. - This response can be the HTML contents of a Web page,
  or a redirect, or a 404 error, or an XML document,
  or an image . . . or anything, really.
  The view itself contains whatever arbitrary logic is necessary to
  return that response.

* We can return HttpResponse by importing HttpResponse from django.http

```python
from django.http import HttpResponse
```

```python
def home_page(request):
    return HttpResponse("Hello Home page")
```

- We can return html page using render from django.shortcut.

```python
from django.shortcuts import render
```

`Functional views Model`

```python
def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request,"leads/lead_list.html",context)
```

## Context

Context is a class within the django.template module of the Django project.<br>
<kbd>Passing context</kbd>

```python
def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    #return HttpResponse("Hello Home page")
    return render(request,"leads/lead_list.html",context)
```

DEFINE Context for each views then we can use that context variable in our html docs.<br>
<kbd>How to Access Context</kbd>

```html
<ul>
  {% for lead in leads %}
  <li>Name : {{lead}}</li>
  {% endfor %}
</ul>
```

## URL Namespace

### Root URL

- Root Url is the `url.py` file present in root folder

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/',include('leads.urls',namespace="leads")),
]
```

- NameSpace is a unique way to find all the urls inside the file
  - To specify the name space we have to add name in our app `urls.py` file.

### App URL

```python
from django.urls import path
from .views import home_page
#app name for namespace in root url
app_name = "leads"

urlpatterns = [
    path('', home_page, name="lead-list"),
]
```

### passing Primary Key may cause error

- if we add another path after lead detail than url is expected as integer but that is string error

```python
path('<int:pk>', lead_detail,
name="lead-detail"),
#after specifying the data type we can add
path('create/', LeadCreateView),

path('<int:pk>/update', lead_update),

path('<int:pk>/delete', lead_delete),
```

## Forms And Create View

The convienient way to setup form logic to to create a file in your app folder by the name `forms.py`.

- import forms

```python
from django import forms
```

- create Form

```python
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
```

- import that form into your `views.py`

```python
from .forms import LeadForm
```

- form is passed as context to the views model whre we use form.

```python
context = {
        "Form":LeadForm()
    }
```

- add form to template
  - \_as_p - show each field wrapped inside paragraph
  - must wrap form context inside form tag.
  - csrf_token is a middleware token for security purpose.

```html
<form method="post">
  {% csrf_token %} {{Form.as_p}}
  <button type="submit">Submit</button>
</form>
```

- Post request send a Query Dictonary with all the data submited in the form.
  - **form.cleaned_data** will retun a clean dictonary.
  - **redirect** is a function inside `django.shortcut` which will redirect us to the link after execution.

```python
def lead_create(request):
    #print(request.POST)
    if request.method == "POST":
        #print("Receiving POST Request")
        form = LeadForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            age = data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent =agent
            )
            #print("lead is created")
            return redirect("/leads")
    context = {
        "Form":LeadForm()
    }
    return render(request,"leads/lead_create.html",context)
```

## Django Modal Form

Modal Form is a built in feature in django which allow us to use existing modal and convert that into form.

- create model

```python
class LeadModelForm(forms.ModelForm):
     class Meta:
        model = Lead
        fields={
            'first_name',
            'last_name',
            'age',
            'agent',
        }
```

- use that modal

```python
from .forms import LeadForm
```

```python
def lead_create(request):
    #print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        #print("Receiving POST Request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            age = data['age']
            agent = data['agent']
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent =agent
            )
            #print("lead is created")
            return redirect("/leads")
    context = {
        "Form":LeadModelForm()
    }
    return render(request,"leads/lead_create.html",context)
```

## Easiest way

- the easiest way is to use `form.save()`
- `.save()` can be used because at he time of defining the modal we gave modal name and field. all the data passed will be save as a new instance of lead.

```python
def lead_create(request):
    #print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        #print("Receiving POST Request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "Form":LeadModelForm()
    }
    return render(request,"leads/lead_create.html",context)
```

- Update

```python
def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        #print("Receiving POST Request")
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "lead":lead,
        "form":form
    }
    return render(request,"leads/lead_update.html",context)
```

- Delete

```python
def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
```

## URl Names

- Easier way than writing hard coded link.

- Url name allow us to reference a particular path in an easy way.
- if we have to change the path link of particular url pattern than the pattern will not break.

```python
urlpatterns = [
    path('', home_page, name="lead-list"),

    path('create/', LeadCreateView, name="lead-create"),

    path('<int:pk>', lead_detail, name="lead-detail"),

    path('<int:pk>/update', lead_update, name="lead-update"),

    path('<int:pk>/delete', lead_delete, name="lead-delete"),
]
```

- Add url using name and namespace

```jsx
{% url 'namespace: url-name'  args %}
```

```html
<button><a href="{% url 'leads:lead-create' %}">Create Lead</a></button>
```

## Extending Template

you can use the same parts of your HTML for different pages of your website.

### Create a base template

- A base template is the most basic template that you extend on every page of your website.
- base template provides consistancy to the project design.
- we can add styles in base template.

```file
-app
-templates
    └───base.html
```

### Blocks

<kbd>base.html</kbd>

```html
<body>
  {% block content%}
  <!-- Only the content we want to include -->
  {% endblock content %}
</body>
```

<kbd>somepage.html</kbd>

```html
{% extends base.html %}
```

Now We can remove all the extra repeted code from html and wrap the code which we want to show.

```html
{% block content %}
<div>Logic Inside</div>
{% endblock content %}
```

- This file will use base.html as reference or base and give output.

### Include some templates inside base template

```html
{% include "navbar.html" %} {% block content %} {%endblock content%} {% include
footer.html%}
```

<center><kbd>---Navbar----</kbd></center>
<center><kbd>---Content---</kbd></center>
<center><kbd>---Footer----</kbd></center>

## Class Based Views

Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:

- Organization of code related to specific HTTP methods (GET, POST, etc.) can be addressed by separate methods instead of conditional branching.
- Object oriented techniques such as mixins (multiple inheritance) can be used to factor code into reusable components.

### Function Base views

```python
def landing_page(request):
    return rneder(request,"landing.html")
```

### converting landing_page view to a class based LandingPage View

- import built in class based generic view template

```python
import django.views.generic import TemplateView
```

- TemplateView takes template name

```python
class LandingPageView(TemplateView):
    template_name = "landing.html"
```

- Now to use hook that view into url
  - import
  - .as_view() allow class to used as views.

```python
urlpattern = [
    path('',LandingPageView.as_view(),name = "landing-page"),
]
```

## Django generic view

Django’s generic views were developed to ease that pain. They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to write too much code.

### Django provides CRUD - L (views) Generic Views

- Create
- Retrive
- Update
- Delete
- List

Import Generic

```python
from django.views import generic
```

### CreateView generic view

```Python
class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")
```

### ListView generic view

```python
class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

```

### DetailView generic view

```python
class LeadDetailView(generic.DetailView):
    template_name = "leads_details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
```

### UpdateView generic view

```python
class UpdateView(generic.UpdateView):
    template_name = "leads.lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
```

### DeleteView generic view

```python
class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
```

## Static Files

Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”.

- Django provides django.contrib.staticfiles to help us manage them.

Step1 : Create a Static folder in root

step2 : Inside `settings.py` Define Static Url if Not Defined.

```python
STATIC_URL = '/static/'
```

step3 : List Of Path Where static files of this project will be held

```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

step4 : set root folder

```python
STATIC_ROOT = "static_root"
```

step5 : To use static file import settings to root urls using that we can reference all static

- STATIC_URL
- STATIC_DIRS
- STATIC_ROOT

```python
from django.conf import settings
```

step5 : Import static in root `urls.py`

```python
from django.conf.urls.static import static
```

step6 : When we are in debug mode our static file will be in static folder but during deployment it may be posible that our static file is in cloud hence

```python
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
```

step7 :In your templates, use the static template tag to build the URL for the given relative path using the configured STATICFILES_STORAGE.

```html
{% load static %} <img src="{% static 'my_app/example.jpg' %}" alt="My image" />
```

<b>[Static Files for Deployment](https://docs.djangoproject.com/en/3.2/howto/static-files/deployment/)
</b>

## [Sending Emails](https://docs.djangoproject.com/en/3.2/topics/email/)

Although Python provides a mail sending interface via the **smtplib module**, Django provides a couple of light wrappers over it. <br>
These wrappers are provided to make sending email extra quick, to help test email sending during development, and to provide support for platforms that can’t use SMTP.

### Setting the email setup

- Whenever a lead is created we will send a mail.

```python
def form_valid(self, form):
        # TODO send mail
        send_mail(
            subject="A lead has been created",
            message="I hope you are okay",
            from_email="test@test.com",
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)
```

**This will give us an error of connection refused.**

- Set a temprory email backend as console but in production we use this:

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
```

- After that we will receive email to console locally.

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

---

# Django Authentication

These steps are involved because in the docs there is everything pre build for these folder structure.

- step1 : Go to root templates folder and create a folder registration.
- step2 : Inside registration create login.html
- step3 : Setup the form
- step4 : import in `urls.py`
  ```python
      import LoginView from django.contrib.auth.views
  ```
- step5 : create a url path
- step6 : Now we can check by authenticating super users
- step7 : After that we have to set after login redirection path in settings.py
