from django.shortcuts import render
from django. http import HttpResponse
from django.template import loader
from . models import classes

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
    