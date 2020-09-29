from django.conf.urls import url

from learnSerializer import views
from learnSerializer.views import GoodsView, helloView

urlpatterns=[
    url(r'^blogs/$', views.BlogsView.as_view()),
    url(r'^blogs/(?P<pk>\d+)/', views.BlogView.as_view()),
    url(r'^goods/',GoodsView.as_view()),
    url(r'^hello/',helloView),
]