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

### Option 2
  1. I'm assuming you just installed Ubuntu 20.04 so make [initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
