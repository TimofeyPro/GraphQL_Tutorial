## Build a Blog Using Django, Vue v3, Vue Router v4, Vue Apollo v4 and GraphQL.  
I tested a tutorial [Build a Blog Using Django, Vue, and GraphQL tutorial](https://realpython.com/python-django-blog/#step-5-set-up-vuejs) by Dane Hillard on Ubuntu 20.04 (LTS) x64 virtual servers in [DigitalOcean](https://www.digitalocean.com/). But since the tutorial uses Vue 2, I rewrote the code using vue<b>@3</b>.2.29, vue-router@<b>4</b>.0.12 and vue/cli-service@4.5.15, 
 
   1. Make [initial server setup](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)
   2. Make [set up of Django with Postgres, Nginx, and Gunicorn on Ubuntu 20.04] (https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04)
   3. Follow steps 1 - 4 from [original tutorial](https://realpython.com/python-django-blog/)
   4. sudo ufw allow 8080(this creates port 8080 which will be used by frontend)
   5. install latest stable version of nude js:
        a.  curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
        b.  sudo apt-get install -y nodejs
   6. sudo npm install -g @vue/cli  
   7. vue create frontend (choose - Default (<b>Vue 3</b>) ([Vue 3] babel, eslint)
   8. cd frontend
   9. vue add router
   10. npm install --save graphql graphql-tag @apollo/client
   11. npm install --save @vue/apollo-composable
   12. npm install --save @vue/apollo-option
   13. npm run serve (check that frontend works at http://IP address of your server 206.81.25.245:8080/
   14. copy 
 


#### [Week2: Linear Regression with multiple variables](https://github.com/TimofeyPro/ML-course-in-Python/tree/master/Exercise2:%20Linear%20Regression%20with%20multiple%20variables)

   1. [Week2: Solution using Numpy and feature normalization](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Exercise2:%20Linear%20Regression%20with%20multiple%20variables/ex1-multi.ipynb)
   2. [Week2: Same solution using Normal Equation](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Exercise2:%20Linear%20Regression%20with%20multiple%20variables/ex1-Norm-Eqv.ipynb)

#### [Week3: Logistic Regression](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Week3:%20Logistic%20Regression)

   1. [Week3: Solution using Gradient Descent](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Week3:%20Logistic%20Regression/W3_Solution%20using%20Gradient%20Descent.ipynb)
   2. [Week3: Same solution using Scikit-Learn](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Week3:%20Logistic%20Regression/W3_Solution%20using%20Scikit-Learn.ipynb)
   3. [Week3: Microchips solution (adding additional higher order polynomial features)](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Week3:%20Logistic%20Regression/microchip.ipynb)

#### [Week4: One-vs-All + Neural Networks](https://github.com/TimofeyPro/ML-course-in-Python/blob/master/Week4:%20One-vs-All%20%2B%20Neural%20Networks/one-vs-all.ipynb)
        
#### [Week 5: Backpropagation](https://github.com/TimofeyPro/coursera_ml_andrew/blob/master/ex4.ipynb)  
