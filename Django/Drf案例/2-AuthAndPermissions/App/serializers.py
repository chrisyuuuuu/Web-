from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from App.models import BlogUser, Blog


class BlogUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password_hash = make_password(validated_data.get('b_password'))
        validated_data['b_password'] = password_hash
        return BlogUser.objects.create(**validated_data)
    class Meta:
        model = BlogUser
        fields = ['id','b_username','b_password']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','b_title','b_content']