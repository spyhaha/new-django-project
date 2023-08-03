# News API

Simple web-application with REST API for creating news

### Installation

[**Python3**](https://www.python.org/) is required including [**Django**](https://docs.djangoproject.com/en/3.2/intro/install/) and [**Django-REST-Framework**](https://www.django-rest-framework.org/#installation):

```bash
$ git clone https://github.com/d-rooX/news-django-project
$ cd news-django-project
$ pip install -r requirements.txt
```

### Migrate database

```bash
$ python manage.py migrate
```

#### To use API you need to authenticate via web-app and extract auth-key from /profile page
#### Make update, delete and create requests with header "Authorization" and value "Token <YOUR_TOKEN>"


> Postman collection: https://www.getpostman.com/collections/50d6953f214e19f1708b 

> Github repository: https://github.com/d-rooX/news-django-project

> Heroku: https://news-django-project.herokuapp.com/
