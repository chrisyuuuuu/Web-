import uuid
from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from App.authentication import BlogUserAuthentication
from App.models import BlogUser, Blog
from App.permissions import BlogUserPermissions
from App.serializers import BlogUserSerializer, BlogSerializer
from App.throttle import AuthThrottle


class UsersAPIView(CreateAPIView):

    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer
    permission_classes = ()
    # throttle_classes = (AuthThrottle,)
    def post(self, request, *args, **kwargs):
        action = request.query_params.get("action")

        if action == "register":
            return self.create(request, *args, **kwargs)
        elif action == "login":
            return self.login(request, *args, **kwargs)
        else:
            raise ValidationError(detail="请提供正确的动作")

    def login(self, request, *args, **kwargs):
        username = request.data.get("b_username")
        password = request.data.get("b_password")
        try:
            user = BlogUser.objects.get(b_username=username)
        except Exception as e:
            raise ValidationError(detail="用户不存在")

        if not user.verify_password(password):
            raise ValidationError(detail="密码错误")

        token = uuid.uuid4().hex

        cache.set(token, user.id, timeout=60*60*24*7)

        data = {
            "msg": "ok",
            "status": HTTP_200_OK,
            "token": token
        }

        return Response(data)
    # def perform_create(self, serializer):
    #     validated_data = serializer.validated_data
    #     b_password = validated_data.get('b_password')
    #     password_hash = make_password(b_password)
    #     validated_data.update({'b_password':password_hash})
    #     serializer.save()


class BlogsAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (BlogUserAuthentication,)
    permission_classes = (BlogUserPermissions,)

    def perform_create(self, serializer):
        serializer.save(b_user=self.request.user)
