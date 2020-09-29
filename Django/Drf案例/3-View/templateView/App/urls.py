from django.conf.urls import url

from App.views import HelloView, TemplateView, HelloListView

urlpatterns = [
    url(r'^hello',HelloView.as_view()),
    url(r'^template',TemplateView.as_view(template_name="hello.html")),
    url(r'^list', HelloListView.as_view()),

]