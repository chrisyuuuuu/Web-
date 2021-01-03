### 1、为什么URL 应该保持整洁和有意义？

```
#命名组
url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive)
views.month_archive(request, year='2005', month='03')
```

**2、捕获的参数永远是字符串**

**3、视图函数默认值**

```
# URLconf
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^blog/$', views.page),
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
]

# View (in blog/views.py)
def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
    ...
```

**4、include**

```
# 正则表达式没有包含$（字符串结束匹配符），但是包含一个末尾的反斜杠。
from django.conf.urls import include, url

urlpatterns = [
    # ... snip ...
    url(r'^community/', include('django_website.aggregator.urls')),
    url(r'^contact/', include('django_website.contact.urls')),
    # ... snip ...
]
```

**5、extra_patterns**

**6、去除URLconf 中的冗余，其中某个模式前缀被重复使用。** 

```
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/', include([
        url(r'^history/$', views.history),
        url(r'^edit/$', views.edit),
        url(r'^discuss/$', views.discuss),
        url(r'^permissions/$', views.permissions),
    ])),
]
```

**7、父url参数传递给子url**

**8、额外的选项给视图函数**

```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
]
# 对于/blog/2005/请求，Django 将调用views.year_archive(request, year='2005', foo='bar'),同样适用include
```

**9、反向解析**

```
url(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),

# 模板
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
# python中使用
reverse('news-year-archive', args=(year,))
```

**10、命名空间**

```
# 即使不同的应用使用相同的URL 名称
url(r'^publisher-polls/', include('polls.urls', namespace='publisher-polls', app_name='polls')),

# 模板
{% url 'polls:index' %}
# 类视图
reverse('polls:index', current_app=self.request.resolver_match.namespace)
```



