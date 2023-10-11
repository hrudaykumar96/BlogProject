from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def read(request):
    read_data=Project.objects.all()
    if request.method=="GET":
        data=request.GET.get("search")
        if data!=None:
            read_data=Project.objects.filter(title__icontains=data)
    return render(request,"home.html", {"read_data":read_data})


def create(request):
    if request.method=="POST":
        title=request.POST['title']
        link=request.POST['link']
        description=request.POST['description']
        if Project.objects.filter(title=title).first():
            return redirect('home')
        c=Project(title=title, link=link, description=description)
        c.save()
        messages.success(request,"Data Created Successfully")
        return redirect('home')
    return render(request,"add.html")


def update(request, id):
    update_data=Project.objects.get(id=id)
    return render(request,"update.html",{"update_data":update_data})


def new_data(request, id):
    if request.method=="POST":
        title=request.POST['title']
        link=request.POST['link']
        description=request.POST.get('description')
        dt=Project.objects.get(id=id)
        dt=Project(id=id, title=title, link=link, description=description)
        dt.save()
        messages.success(request,"Data Updated Successfully")
        return redirect('home')
    return render(request, 'update.html')



def remove(request, id):
    if request.method=="GET":
        del_data=Project.objects.get(id=id)
        del_data.delete()
        messages.success(request, "Data Deleted Successfully")
        return redirect('home')
    return render(request,"home.html")