from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse("Hello World")
l=[]
def fun2(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(fun2)
    else:
        return render(request,'demo.html')
def fun3(request):
    return render(request,'about.html')
def fun4(request):
    return render(request,'contact.html')

l=[{'name':'aa','age':'22'},{'name':'ba','age':'32'}]
def display(request):
    a='welcome'
    return render(request,'display.html',{'data':l,'data1':a})

def add_dtls(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        return redirect(display)
    else:
        return render(request,'add_dtls.html')