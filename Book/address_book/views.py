from django.shortcuts import render,render_to_response,redirect
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from .models import Contact
import csv


def dumpData(request):
    with open('data.csv', 'r') as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            print(row)
            a = Contact(name=row[0],phone=row[1])
            try:
                a.save()
            except:
                print("Error")
    return HttpResponse("Success")

def getobject():
    contacts = Contact.objects.all().order_by("name")
    data = [{"id":j.id,"name": j.name, "phone": j.phone } for j in contacts]
    return data
def getData(request):
    if request.method == "GET":
        data=getobject()
        return render(request, 'address_book/index.html' , {"data": data})
    elif request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        newcontact = Contact(name=name, phone=phone)
        try:
            newcontact.save()
        except:
            data=getobject()
            return render(request, 'address_book/index.html' ,  {"data": data,"error": "Error"})
        data=getobject()
        return render(request, 'address_book/index.html' , {"data": data})

def updateData(request, id):
    if request.method == "GET":
        obj=Contact.objects.get(id=id)
        return render(request, 'address_book/update.html', {"data": obj})
    else:
        print("updated")
        if request.POST.get('name'):
            name=request.POST.get('name')
            obj=Contact.objects.get(id=id)
            obj.name=name
            obj.save()
        if request.POST.get('phone'):
            phone=request.POST.get('phone')
            obj=Contact.objects.get(id=id)
            obj.phone=phone
            obj.save()
        data=getobject()
        return render(request, 'address_book/index.html',{"data": data})


def deleteData(request, id):
    if Contact.objects.filter(id=id).exists():
        Contact.objects.get(id=id).delete()
        data=getobject()
        return HttpResponseRedirect('/address/getdata')
    else:
        raise Http404
