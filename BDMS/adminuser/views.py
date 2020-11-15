from django.shortcuts import render,HttpResponseRedirect
from .models import adminmodel
from django.http import JsonResponse
from core import views
from core.models import donarmodel,contactmodel
from django.contrib import messages
contact_no="9999999999"
contact_email="abc@gmail.com"
about_details="This is about Details"
# Create your views here.

def admin_login(request):
    if request.session.get('is_admin_login',False)==True:
        return JsonResponse({'status':3})
    else:
        if request.method=="POST":
            eml=request.POST['email']
            pwd=request.POST['password']
            adm=adminmodel.objects.filter(email=eml,password=pwd)
            if adm.count() == 1:
                request.session['is_admin_login']=True
                request.session['admin_email']=eml
                return JsonResponse({'status':1})
            elif adm.count() == 0:
                return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':2})
            


def dashboard(request):
    views.title="dashboard"
    heading="Dashboard"
    if request.session.get('is_admin_login',False)==True:
        donars=donarmodel.objects.all()
        queries=contactmodel.objects.all()
        return render(request,'adminuser/dashboard.html',{'title':views.title,'dnr':donars.count(),
        'qry':queries.count(),'heading':heading})
    else:
        return HttpResponseRedirect('/')



def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')


def add_donar(request):
    if request.session.get('is_admin_login',False)==True:
        views.title='Add Donar'
        heading="Add New Donar"
        if request.method=="POST":
            nm=request.POST['name']
            ph=request.POST['phone']
            em=request.POST['email']
            age=request.POST['age']
            gen=request.POST['gender']
            bgr=request.POST['bgroup']
            address=request.POST['address']
            msg=request.POST['message']
            img=request.FILES['image']
            dr=donarmodel(name=nm,phone=ph,email=em,age=age,gender=gen,bgroup=bgr,address=address,message=msg,image=img)
            dr.save()
            messages.success(request,'Donar Added Successfully !!!')
            return HttpResponseRedirect('/adminuser/adddonar/')
        else:
            return render(request,'adminuser/adddonar.html',{'title':views.title,'heading':heading})
    else:
        return HttpResponseRedirect('/')
        

def donar_list(request):
    if request.session.get('is_admin_login',False)==True:
        views.title='Donar List'
        heading="List Of Donars"
        donars=donarmodel.objects.all()
        return render(request,'adminuser/donarlist.html',{'title':views.title,'heading':heading,'donars':donars})
    else:
        return HttpResponseRedirect('/')


def delete_donar(request,id):
    if request.session.get('is_admin_login',False)==True:
        pi=donarmodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/donarlist/')
    else:
        return HttpResponseRedirect('/')
    

def query_list(request):
    if request.session.get('is_admin_login',False)==True:
        views.title='Query List'
        heading="List Of Queries"
        queries=contactmodel.objects.all()
        return render(request,'adminuser/queries.html',{'title':views.title,'heading':heading,'queries':queries})
    else:
        return HttpResponseRedirect('/')


def delete_query(request,id):
    if request.session.get('is_admin_login',False)==True:
        pi=contactmodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/adminuser/querylist/')
    else:
        return HttpResponseRedirect('/')


def admin_change_pass(request):
    if request.session.get('is_admin_login',False)==True:
        views.title='Change Password'
        heading="Change Password"
        eml=request.session['admin_email']
        if request.method=="POST":
            newpass=request.POST['newpass']
            pi=adminmodel.objects.get(email=eml)
            pi.password=newpass
            pi.save()
            messages.success(request,'Password Changed Successfylly !!!')
            return HttpResponseRedirect('/adminuser/changepass/')
        else:
            return render(request,'adminuser/adminchangepass.html',{'title':views.title,'heading':heading,'eml':eml})
    else:
        return HttpResponseRedirect('/')



def update_contact(request):
    if request.session.get('is_admin_login',False)==True:
        views.title='Update Contact Us'
        heading="Update Contact Us"
        return render(request,'adminuser/updatecontact.html',{'title':views.title,'heading':heading})
    else:
        return HttpResponseRedirect('/')


def new_contact_details(request):
    if request.method=="POST":
        global contact_no
        contact_no=request.POST['mob']
        global contact_email
        contact_email=request.POST['eml']
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



def update_about_us(request):
    if request.session.get('is_admin_login',False)==True:
        views.title='Update About Us'
        heading="Update About Us"
        return render(request,'adminuser/updateaboutus.html',{'title':views.title,'heading':heading})
    else:
        return HttpResponseRedirect('/')



def new_about_details(request):
    if request.method=="POST":
        global about_details
        about_details=request.POST['newabt']
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})