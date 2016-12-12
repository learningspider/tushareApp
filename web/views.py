#_*_coding:utf-8_*_
from django.shortcuts import render
from django.http import HttpResponse
from tushareTools import get_stock_basics as ttget_stock_basics
# Create your views here.
def index(request):
    g= ttget_stock_basics.get_sina_dd()
    if request.user.is_authenticated():
        return render(request, 'base.html',{'g':g})
    return render(request, 'base.html',{'g':g})

def webindex(request):
    return HttpResponse("world")
