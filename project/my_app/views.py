from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse("Hello World")
def fun2(request):
    return render(request,'demo.html')
def fun3(request):
    return render(request,'about.html')
def fun4(request):
    return render(request,'contact.html')