from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from .models import Book, User, Author, Publisher, Client, Sale
import locale


class UserResource(ModelResource):
    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password']
        allowed_methods = ['get', 'post', 'delete']


class BookResource(ModelResource):

    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete', 'put']
        
    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()


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
        allowed_methods = ['get', 'post', 'delete', 'put']
        
    def dehydrate_total_price(self, bundle):
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        return locale.currency(bundle.data['total_price'])


class AuthorResource(ModelResource):

    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        authorization = Authorization()
