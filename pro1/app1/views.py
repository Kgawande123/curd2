from django.http import HttpResponse
from django.shortcuts import render,redirect
from.forms import EmployeeForm
from .models import Employee

# Create your views here.
def eview(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv")
    return render(request,"app1/Employee.html",{"form":form})


def sview(request):
    emp = Employee.objects.all()
    print(emp)
    return render(request,"app1/show.html",{"obj":emp})

def uview(request,pk):
    obj = Employee.objects.get(eid=pk)
    print(obj)
    form = EmployeeForm(instance=obj)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv")
    return render(request,'app1/Employee.html',{"form":form})


def dview(request,k):
    obj = Employee.objects.get(eid=k)
    if request.method =="POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,'app1/success.html',{"obj":obj})