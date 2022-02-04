import strawberry
import strawberry_django
from strawberry_django import auto, auth
from . import models
from typing import List, Optional
from datetime import date
from django.contrib.auth import get_user_model


@strawberry.django.type(get_user_model())
class UserType:
    id: auto
    username: auto
    first_name: auto
    last_name: auto
    is_superuser: auto
    is_staff: auto
    email: auto
    is_active: auto
    profile: auto
    
    
@strawberry.django.type(models.Profile)
class AuthorType:
    id: auto
    user: 'UserType'
    website: auto
    bio: auto
    post_set: List['PostType']

@strawberry.django.type(models.Tag)
class TagType:
    id: auto
    name: auto
  
@strawberry.django.type(models.Post)
class PostType:
    id: auto
    title: auto
    subtitle: auto
    slug: auto
    body: auto
    meta_description: auto
    date_created: auto
    date_modified: auto
    publish_date: auto
    published: auto
    author: 'AuthorType'
    tags: List['TagType']

def get_all_posts(root, info):
    return(
        models.Post.objects.prefetch_related('tags')
        .select_related('author')
        .all()
    )

def author_by_username(root, info, username: str):
    return models.Profile.objects.select_related('user').get(
        user__username=username
    )

def post_by_slug(root, info, slug: str):
    return (
        models.Post.objects.prefetch_related('tags')
        .select_related('author')
        .get(slug=slug)
    )

def posts_by_author(root, info, username: str):
    return (
        models.Post.objects.prefetch_related('tags')
        .select_related("author")
        .filter(author__user__username=username)
    )

def posts_by_tag(root, info, tag: str):
    return (
        models.Post.objects.prefetch_related('tags')
        .select_related('author')
        .filter(tags__name__iexact=tag)
    )


@strawberry.type
class Query:
    all_posts: List[PostType] = strawberry.django.field(resolver=get_all_posts)
    author_by_username: Optional[AuthorType] = strawberry.django.field(resolver=author_by_username)
    post_by_slug: 'PostType' = strawberry.django.field(resolver=post_by_slug)
    posts_by_author: List[PostType] = strawberry.django.field(resolver=posts_by_author)
    posts_by_tag: List[PostType] = strawberry.django.field(resolver=posts_by_tag)
 
schema = strawberry.Schema(query=Query)
