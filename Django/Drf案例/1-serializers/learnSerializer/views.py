
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from learnSerializer.models import Blog, Goods
from learnSerializer.serializers import BlogSerializer, GoodsSerializer


class BlogsView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self,request):

        b_title = request.POST.get('b_title')
        b_content = request.POST.get('b_content')

        # blog = Blog.objects.create(b_content=b_content,b_title=b_title)
        # serializer = BlogSerializer(blog)
        # return JsonResponse(serializer.data)
        data = {
            'b_title':b_title,
            'b_content':b_content
        }
        serializer = BlogSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse({'msg':'验证失败'})
        serializer.save()
        return JsonResponse(serializer.data)

class BlogView(View):
    def get(self,request,pk):
        blogs = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blogs)

        return JsonResponse(serializer.data)

    def delete(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()

        return JsonResponse(data={'msg':'delete ok'},status=204)

    def put(self, request,pk):

        blog = Blog.objects.get(pk=pk)
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error_messages)
class GoodsView(View):
    def get(self,request):
        goods = Goods.objects.all()
        serializer = GoodsSerializer(goods,many=True)

        return JsonResponse(serializer.data,safe=False)
    def post(self,request):
        g_name = request.POST.get('g_name')
        g_price = request.POST.get('g_price')

        data = {
            'g_name':g_name,
            'g_price':g_price
        }
        serializer = GoodsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error_messages)


# @api_view(['GET','POST'])
def helloView(request):

    data = {
        'msg':'666',
    }

    return JsonResponse(data,status=status.HTTP_200_OK)
