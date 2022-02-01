import strawberry
import strawberry_django
from strawberry_django import auto, auth
from . import models
from typing import List
from datetime import date
from django.contrib.auth import get_user_model

UserType = get_user_model()

@strawberry.django.type(models.Profile)
class AuthorType:
    user: str
    website: str
    bio: str

@strawberry.django.type(models.Tag)
class Tag:
    name: str
  
@strawberry.django.type(models.Post)
class PostType:
    title: str
    subtitle: str
    slug: str
    body: str
    meta_description: str
    date_created: date
    date_modified: date
    publish_date: date
    published: bool
    author: 'AuthorType'
    tags: List['Tag']


@strawberry.type
class Query:
    allPosts: List[PostType]= strawberry.django.field()

schema = strawberry.Schema(query=Query)
