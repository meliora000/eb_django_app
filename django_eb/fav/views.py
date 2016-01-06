from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader,Context
# Create your views here.

def index(request):
    return render(request,"fav/favorite.html",{})
