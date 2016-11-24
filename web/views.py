#_*_coding:utf-8_*_
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request,'prize/index.html',{'user':request.user})
    return render(request, 'base.html')

def webindex(request):
    return HttpResponse("world")
