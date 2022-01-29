## Build a Blog Using Django, Vue v3, Vue Router v4, Vue Apollo v4 and GraphQL.  
I tested a tutorial [Build a Blog Using Django, Vue, and GraphQL tutorial](https://realpython.com/python-django-blog/#step-5-set-up-vuejs) by Dane Hillard on Ubuntu 20.04 (LTS) x64 virtual servers in [DigitalOcean](https://www.digitalocean.com/). But since the tutorial uses Vue 2, I rewrote the code using vue<b>@3</b>.2.29, vue-router@<b>4</b>.0.12 and vue/cli-service@4.5.15, 
 
   1. Make [initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
   2. Make [set up of Django with Postgres, Nginx, and Gunicorn on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)
   3. Follow steps 1 - 4 from [original tutorial](https://realpython.com/python-django-blog/)
   4. sudo ufw allow 8080 (this opens port 8080 which will be used by frontend)
   5. install latest stable version of nude js:
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
   14. copy and study App.vue, main.js and router.js from this repository [GraphQL_Tutorial/frontend/src/](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/frontend/src)
   15. vue files in components folder were not changed but also saved [here](https://github.com/TimofeyPro/GraphQL_Tutorial/tree/main/frontend/src/components)

Thats all.
