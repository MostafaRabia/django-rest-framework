from django.contrib.auth.models import User, Group
from rest_framework import serializers
from books.models import Book
from products.models import Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', queryset=Book.objects.all())
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'books', 'products']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
