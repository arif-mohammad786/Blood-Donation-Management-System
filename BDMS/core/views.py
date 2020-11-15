from django.shortcuts import render,HttpResponseRedirect
from .models import donarmodel,contactmodel
from django.contrib import messages
from django.http import JsonResponse
from adminuser import views
# global variable 
global title

# Create your views here.
def home(request):
    global title
    title="home"
    donars=donarmodel.objects.all()[:3]
    return render(request,'core/home.html',{'title':title,'donars':donars})

def about(request):
    global title
    title="about"
    return render(request,'adminuser/aboutus.html',{'title':title,'about_details':views.about_details})


def whydonar(request):
    global title
    title="whydonar"
    return render(request,'core/whydonar.html',{'title':title})


def become_donar(request):
    global title
    title="becomedonar"
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
        messages.success(request,'Congratulation You Have Successfully Registered !!!')
        return HttpResponseRedirect('/core/becomedonar/')

    return render(request,'core/becomedonar.html',{'title':title})


def searchdonar(request):
    global title
    title="searchdonar"
    if request.method=="POST":
        donars=donarmodel.objects.filter(bgroup=request.POST['searchgroup'])
        count=donars.count()
        return render(request,'core/searchdonar.html',{'title':title,'donars':donars,'count':count})   
    return render(request,'core/searchdonar.html',{'title':title})


def contact(request):
    global title
    title="contact"
    if request.method=="POST":
        name=request.POST['name']
        ph=request.POST['mobile']
        eml=request.POST['email']
        ms=request.POST['message']
        msg=contactmodel(name=name,phone=ph,email=eml,message=ms)
        msg.save()
        messages.success(request,'Message Sent Successfully !!!')
        return HttpResponseRedirect('/core/contact/')
    return render(request,'adminuser/contactus.html',{'title':title,'mob':views.contact_no,'eml':views.contact_email})