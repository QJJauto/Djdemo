from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse         #需要导入HttpResponse模块

def hello(request):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    return HttpResponse("Hello world ! ")

def test(request):                          #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
    return HttpResponse("test ! ")


def process_parameters(body):
     try:
         body_dic = {}
         key_values = str(body).split("&")
         for key_value in key_values:
             body_dic[key_value.split("=")[0]] = key_value.split("=")[1]
         return body_dic
     except Exception as e:
         return e