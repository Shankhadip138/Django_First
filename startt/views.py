from django.shortcuts import render
#from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader



def starting(request):
    return render(request,'starting.html')
