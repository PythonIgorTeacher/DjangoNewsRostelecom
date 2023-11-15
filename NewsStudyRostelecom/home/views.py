from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm, Demo

def index(request):
    return render(request,'general.html')

def demoform(request):
    form = DemoForm()
    if request.method == 'POST':

        new_model = DemoForm(request.POST,request.FILES)
        new_model.save()

    context = {'form':form}
    return render(request,'home/image_Form.html',context)


def showlastmodel(request):
    model = Demo.objects.all().first()
    context = {'model':model }
    return render(request,'home/image_Form.html',context)