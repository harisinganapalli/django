from django.shortcuts import render,redirect
from django. http import HttpResponse
from django.template import loader
from . models import classes
from .models import new
from .forms import Employeeform
from .forms import Student


# Create your views here.
def function(request):
        # return HttpResponse("Hello world!")
#  template=loader.get_template('first.html')
# return HttpResponse(template.render())  for  instead using of 8,9   use line 10
#   return render( request,'first.html')
    mymembers = classes.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, "templatecall.html", context)

def testing(request):
    context={
        'firstname':"hari"

    }
    return render (request,'datacall.html',context)

def test(request):
    myname=classes.objects.all().values()
    context={
        'mymembers': myname,
    }
    return render( request,'templatecall.html',context)

def tag(request):
    
    return render (request,'conditions.html',{'greeting':1})
def common(request):
    context={
        'great':20,
        'great':10

    }
    return render(request,'conditions.html',context)
def proper(request):
    context={
        'greeting':1,
        'hold':2,
        'happy':1,
        'lessthan':3,
        'greaterthan':6,
        
    }
    return render(request,'condition1.html',context)

def loops(request):
    context={
        'fruits': ['apple','mango','banana','watermelon','kiwi']
       
    }
    return  render(request,'loop.html', context)


def query(request):
    querysets=classes.objects.all().values()
    context={
        'set':querysets,
    }
    return render(request,'queryset.html',context)

def particular(request):
    here=classes.objects.values_list('phone')
    context={
        'hari':here,
    }   
    return render(request,'getdata.html',context)

def rare(request):
    help= new.objects.filter(name='hari').values()
    print(help)
    context={
        'set':help,
    }
    return render(request,'getfilter.html',context)
def bootstrap(request):
    querysets=classes.objects.all().order_by('lastname').values()
    context={
        'set':querysets,
    }
    return render(request,'queryset.html',context)
def boot(request):
    querysets=classes.objects.all().order_by('-lastname').values()
    context={
        'set':querysets,
    }
    return render(request,'queryset.html',context)
def stylecss(request):
    context={
        'animals': ['lion','tiger','peacock','cat','dog','elephant','cow']

    }
    return render(request,'style.html',context)

def employeelist(request):
    
    form=Employeeform()
    if request.method=='POST':
       print(request.POST['position'])
       fullname=request.POST['fullname']
       print(fullname)
       employeecode=request.POST['employeecode']
       print(employeecode)
       number=request.POST['number']
       print(number)
       position=request.POST.get('position')
       print(position)
       form= Employeeform(request.POST)
       print(form)
       if form.is_valid():
            print("enters")
            form.save()
            print("data inserted")

            return redirect('/')
       else:

           form=Employeeform()
           return render(request,'employeelist.html',{'form':form})
    return render(request,'employeelist.html',{'form':form})   
    # else:
    #     form=Employeeform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect()   

def employeeform(request):
    # form = Employeeform()
    # print(form)
    return  render(request,'employeeform.html',) 
def employeedelete(request):
    return render(request,'employeedelete',)


def studentform(request):
    form=Student()
    if request.method=='POST':
        print(request.POST)
        form = Student(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("data inserted")
            return HttpResponse('Student form submitted successfully')
    else:
        student=Student() 
        return render(request,'students.html',{"form":student})
    return render(request,'students.html',{"form":form})
         

