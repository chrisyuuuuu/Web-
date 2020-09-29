from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from App.models import Book
from App.serializers import UserSerializers, GroupSerializers, BookSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers