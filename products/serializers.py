from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(view_name='user-detail', many=True, queryset=User.objects.all())

    class Meta:
        model = Product
        fields = ['url', 'users', 'name']
