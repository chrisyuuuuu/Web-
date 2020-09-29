from django.conf.urls import url

from App.views import UsersAPIView, BlogsAPIView

urlpatterns = [
    url(r'^users/',UsersAPIView.as_view()),
    url(r'^blogs/',BlogsAPIView.as_view()),
]