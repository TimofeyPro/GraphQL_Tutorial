## Deploying a separate backend [Django 4.x, PostgreSQL 12.9, Gunicorn, Nginx и django-cors-headers] and frontend [Node.js LTS (16.x), @vue/cli (Vue CLI), Vue v3, Vue Router v4 и Vue Apollo v4] using Strawberry as GraphQL API 

I tested [Build a Blog Using Django, Vue, and GraphQL tutorial](https://realpython.com/python-django-blog/#step-5-set-up-vuejs) by Dane Hillard on Ubuntu 20.04 (LTS) x64 virtual server in [DigitalOcean](https://www.digitalocean.com/). But since the tutorial uses Django 3.x, Vue 2 and Graphene-Django (which is not sufficiently supported now), I rewrote the code using the latest versions available at the end of January 2022 and has replaced Graphene-Django with [Strawberry](https://strawberry.rocks/):
- [Django==4.0.2](https://docs.djangoproject.com/en/4.0/)
- [strawberry-graphql-django 0.2.5](https://github.com/strawberry-graphql/strawberry-graphql-django)
- [Node.js LTS (16.x)](https://github.com/nodesource/distributions)
- [@vue/cli-service@4.5.15](https://cli.vuejs.org/)
- [vue@3.2.29](https://v3.vuejs.org/)
- [vue-router@4.0.12](https://next.router.vuejs.org/)
- @apollo/client@3.5.8
- @vue/apollo-composable@4.0.0-alpha.16
- [@vue/apollo-option@4.0.0-alpha.16](https://v4.apollo.vuejs.org/)

Since the backend and frontend in this example work completely independently, we can test their operations separately. This will also allow you to better understand how each component works. You have two options:
<br> Option 1 - leave backend with Graphene-Django unchanged, as in [the original exercise](https://realpython.com/python-django-blog/), and change only frontend
<br> Option 2 - completely change both backend and frontend, i.e. we will use Django 4.x, Poetry, Strawberry, Vue v3 and Vue Apollo v4.

### Option 1
Next, I provide a list of necessary actions for the initial setup of a remote virtual server and the creation of a new frontend part:
 
   1. Make [initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
   2. Make [set up of Django with Postgres, Nginx, and Gunicorn on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04). Your should install Django==3.1.7 for this Option.
   3. Follow steps 1 - 4 from [original tutorial](https://realpython.com/python-django-blog/)
   4. sudo ufw allow 8080 (this opens port 8080 which will be used by frontend)
   5. install latest stable version of [nude.js](https://github.com/nodesource/distributions):
        <br>   a.  curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
        <br>   b.  sudo apt-get install -y nodejs
   6. sudo npm install -g @vue/cli  
   7. vue create frontend (choose - Default (<b>Vue 3</b>) ([Vue 3] babel, eslint)
   8. cd frontend
   9. Install Vue Router and Apollo:
``` 
 ~/backend$ vue add router
 ~/backend$ npm install --save graphql graphql-tag @apollo/client
 ~/backend$ npm install --save @vue/apollo-composable
 ~/backend$ npm install --save @vue/apollo-option
```
   10. **npm run serve** (check that frontend works well at http://<i> IP_address_of_your_server</i>:8080/
   11. copy and study App.vue, main.js and router.js from this repository at [GraphQL_Tutorial/frontend/src/](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/frontend/src)
   12. vue files in components folder (Vue Components as per Steps 7 & 8) were not changed but also saved [here](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/frontend/src/components)

Thats all.

### Option 2 (Django 4.x, Poetry, Strawberry, Vue.js v3.x and Vue Apollo v4)
  1. I'm assuming you just installed Ubuntu 20.04 so make [initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
  2. Install Python, PostgreSQL, Nginx, [cURL](https://curl.se/docs/faq.html), tree:
```
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl tree
```
  3. Make Postgres database setup (you need to define myprojectuser, myproject and 'password' and copy them in settings.py later):
```sql
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```
  4. Install [Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
```
sudo apt install python3.8-venv
sudo curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/your_user_name/.local/bin:$PATH"
echo $PATH
poetry --version
``` 
  5. Create project **backend** with virtual environment and install Django in it:
```
mkdir backend
cd backend
~/backend$ poetry init --no-interaction --dependency Django==4.0.2
~/backend$ poetry install
~/backend$ poetry shell
(backend-...-py3.8) ~/backend$ django-admin startproject backend ~/backend
(backend-...-py3.8) ~/backend$ tree -L 2
(backend-...-py3.8) ~/backend$ poetry add psycopg2-binary
``` 
  6. Make changes in settings.py for ALLOWED_HOSTS, DATABASES and STATIC_ROOT
```python
nano backend/settings.py
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATIC_URL = '/static/'
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
``` 
  7. Run Django Migrations, create Superuser and see the default Django index page:
```PowerShell
(backend-...-py3.8) ~/backend$ python manage.py makemigrations
(backend-...-py3.8) ~/backend$ python manage.py migrate
(backend-...-py3.8) ~/backend$ python manage.py createsuperuser
(backend-...-py3.8) ~/backend$ python manage.py collectstatic
sudo ufw allow 8000
(backend-...-py3.8) ~/backend$ python manage.py runserver 0.0.0.0:8000
``` 
  8. Creating systemd Socket and Service Files for Gunicorn
```PowerShell
(backend-...-py3.8) ~/backend$ poetry add gunicorn
(backend-...-py3.8) ~/backend$ poetry show --tree
sudo nano /etc/systemd/system/gunicorn.socket
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
``` 
```PowerShell
(backend-...-py3.8) ~/backend$ poetry env info
sudo nano /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=your_user_name
Group=www-data
WorkingDirectory=/home/your_user_name/backend
ExecStart=/home/your_user_name/.cache/pypoetry/virtualenvs/backend-...-py3.8/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          backend.wsgi:application

[Install]
WantedBy=multi-user.target
```
```PowerShell
sudo ln -s /etc/nginx/sites-available/backend /etc/nginx/sites-enabled
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
``` 
  9. Configure Nginx to Proxy Pass to Gunicorn
```PowerShell
sudo nano /etc/nginx/sites-available/backend
server {
    listen 80;
    listen [::]:80;
    server_name your_server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/your_user_name/backend;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```  
```PowerShell
sudo ln -s /etc/nginx/sites-available/backend /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo ufw status verbose
```
At this stage you should be able to access your site and see Django welcome page.

  10. Create the Django Blog Application (use <poetry shell> command to access virtual environment) 
```python
(backend-...-py3.8) ~/backend$ python manage.py startapp blog
(backend-...-py3.8) ~/backend$ nano backend/settings.py
 INSTALLED_APPS = [
  ...
  'blog',
]
``` 
  11. Study and copy blog/models.py and blog/admin.py from [here](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/backend/blog).
  12. Study and copy blog/schema.py from [here](https://github.com/TimofeyPro/GraphQL_Tutorial/blob/main/backend/blog/schema.py). Then install Strawberry and django-cors-headers:
```python
(backend-...-py3.8) ~/backend$ poetry add strawberry-graphql-django
(backend-...-py3.8) ~/backend$ poetry add django-cors-headers
nano backend/settings.py
INSTALLED_APPS = [
  ...
  'strawberry.django',
  'corsheaders',
]
MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  ...
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://your_server_domain_or_IP:8080',
]
```
```python
nano backend/urls.py
 
from django.contrib import admin
from django.urls import include, path
from strawberry.django.views import AsyncGraphQLView
from django.views.decorators.csrf import csrf_exempt
from blog.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(AsyncGraphQLView.as_view(schema=schema))),
]
``` 
  
  13. Refresh Django and Gunicorn: 
``` 
(backend-...-py3.8) ~/backend$ python manage.py makemigrations
(backend-...-py3.8) ~/backend$ python manage.py migrate
(backend-...-py3.8) ~/backend$ python manage.py collectstatic
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
``` 
  14. Visit to http://your_server_domain_or_IP/admin and add (input) at least three posts
 
  15. Visit to http://your_server_domain_or_IP/graphql and review your Query. This is your GraphQL API endpoint.
 
  16. Thats all for backend. Then do actions 4-12 from Option 1 and you should see your blog up and running
 
  17. Your backend folder structure should be as follows:
 ```
~/backend$ tree -L 2
├── backend
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── schema.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── poetry.lock
├── pyproject.toml
└── static
    ├── admin
    └── graphiql.html

``` 

 ### Usefull notes to understand above better:
* Graphene-Django has [DjangoObjectType](https://github.com/TimofeyPro/GraphQL_Tutorial/blob/main/backend/blog/schema_graphene.py) which includes all the fields in the model by default. In [this Strawberry schema.py]( https://github.com/TimofeyPro/GraphQL_Tutorial/blob/main/backend/blog/schema.py) we have defined each field separately.
* To restrict users from accessing the GraphQL API page the standard Django [LoginRequiredMixin](https://docs.graphene-python.org/projects/django/en/latest/authorization/) can be used
