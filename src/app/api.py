from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import Book, User, Author


class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class BookResource(ModelResource):

    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        authorization = Authorization()


class AuthorResource(ModelResource):

    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        authorization = Authorization()
