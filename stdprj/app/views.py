from django.shortcuts import render,redirect
from . models import *
# Create your views here.


std=[]

def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        place=req.POST['place']
        # std.append({'roll_no':roll,'name':name,'age':age,'place':place})
        data=Student.objects.create(roll_no=roll,name=name,age=age,place=place)
        data.save
        return redirect(home)
    else:
        data=Student.objects.all()
        return render(req,'home.html',{'student':data})

def edit_std(req,id):
    # data=''
    # for i in std:
    #     if i['roll_no']==a:
    #         data=i
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        place=req.POST['place']
        # data['roll_no']=roll
        # data['name']=name
        # data['age']=age
        # data['place']=place
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age,place=place)
        return redirect(home)
    else:
        data=Student.objects.get(pk=id)
        return render(req,'edit.html',{'data':data})

def delete(req,id):
    # for i in std:
    #     if i['roll_no']==a:
    #         std.remove(i)
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(home)