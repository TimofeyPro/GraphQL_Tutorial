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
   2. Make [set up of Django with Postgres, Nginx, and Gunicorn on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)
   3. Follow steps 1 - 4 from [original tutorial](https://realpython.com/python-django-blog/)
   4. sudo ufw allow 8080 (this opens port 8080 which will be used by frontend)
   5. install latest stable version of [nude.js](https://github.com/nodesource/distributions):
        <br>   a.  curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
        <br>   b.  sudo apt-get install -y nodejs
   6. sudo npm install -g @vue/cli  
   7. vue create frontend (choose - Default (<b>Vue 3</b>) ([Vue 3] babel, eslint)
   8. cd frontend
   9. vue add router
   10. npm install --save graphql graphql-tag @apollo/client
   11. npm install --save @vue/apollo-composable
   12. npm install --save @vue/apollo-option
   13. npm run serve (check that frontend works well at http://<i>IP address of your server</i>:8080/
   14. copy and study App.vue, main.js and router.js from this repository at [GraphQL_Tutorial/frontend/src/](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/frontend/src)
   15. vue files in components folder (Vue Components as per Steps 7 & 8) were not changed but also saved [here](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/frontend/src/components)

Thats all.

### Option 2 (Django 4.x, Poetry, Strawberry, Vue.js v3.x and Vue Apollo v4)
  1. I'm assuming you just installed Ubuntu 20.04 so make [initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
  2. Install Python, PostgreSQL, Nginx, [cURL](https://curl.se/docs/faq.html), tree:
```
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl tree
```
  3. Make Postgres database setup (you need to define myprojectuser, myproject and 'password' and copy them in settings.py later):
```
sudo -u postgres psql
postgres=# CREATE DATABASE myproject;
postgres=# CREATE USER myprojectuser WITH PASSWORD 'password';
postgres=# ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
postgres=# ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE myprojectuser SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
postgres=# \q
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
```
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
```
(backend-...-py3.8) ~/backend$ python manage.py makemigrations
(backend-...-py3.8) ~/backend$ python manage.py migrate
(backend-...-py3.8) ~/backend$ python manage.py createsuperuser
(backend-...-py3.8) ~/backend$ python manage.py collectstatic
sudo ufw allow 8000
(backend-...-py3.8) ~/backend$ python manage.py runserver 0.0.0.0:8000
``` 
  8. Creating systemd Socket and Service Files for Gunicorn
```
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
```
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
```
sudo ln -s /etc/nginx/sites-available/backend /etc/nginx/sites-enabled
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
``` 
  9. Configure Nginx to Proxy Pass to Gunicorn
```
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
```
sudo ln -s /etc/nginx/sites-available/backend /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
sudo ufw status verbose
```
  10. Create the Django Blog Application
  11. . . . . . .. . . ... work in progress...
