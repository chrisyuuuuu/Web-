from django.contrib.auth.models import User, Group
from rest_framework import serializers

from App.models import Book


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','group']
class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']
class BookSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url','b_name','b_price']