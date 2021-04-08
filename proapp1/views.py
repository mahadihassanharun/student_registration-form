from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from proapp1.models import Person
from django.contrib import messages
from .forms import user_form


# Create your views here.
def index(request):
    return render(request,'home.html')
    

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method=="POST":
        name=request.get(['name'])
        email=request.get(['email'])
        phone=request.get(['phone'])
        
        person=Person(name=name,email=email,phone=phone)
        person.save()
        messages.success(request,'user has been register successfully')
        
    return render(request,'register.html')


        # form=user_form(request.POST)
        # if form.is_valid():
        #    return HttpResponseRedirect("this is my 1st priject")

        # else:
        #     return HttpResponseRedirect("form is not valied") 


        # return render(request,'register.html',{"form":form})

    
    # if request.method=="GET":
    #     name=request.GET['name']
    #     email=request.GET['email']
    #     phone=request.GET['phone']
        
        # person=Person(name=name,email=email,phone=phone)
        # person.save()
        # messages.success(request,'user has been register successfully')

        # if person=Person(name=name,email=email,phone=phone)
        #    person.save()
        #    messages.success(request,'user has been register successfully')
        #    return redirect('contact.html')

    

        # name=request.POST.get('name')
        # email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # # user =user.objects.create_user(name=name,email=email,phone=phone)

        # student= student.objects.create_student(name=name,email=email,phone=phone)
        # student.save()
        # 