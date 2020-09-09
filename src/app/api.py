from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import Book, User, Author, Publisher, Client, Sale


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


class PublisherResource(ModelResource):

    class Meta:
        queryset = Publisher.objects.all()
        resource_name = 'publisher'
        authorization = Authorization()


class ClientResource(ModelResource):

    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        authorization = Authorization()


class SaleResource(ModelResource):

    class Meta:
        queryset = Sale.objects.all()
        resource_name = 'author'
        authorization = Authorization()


class AuthorResource(ModelResource):

    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        authorization = Authorization()
