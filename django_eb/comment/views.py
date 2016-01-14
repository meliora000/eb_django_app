from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json

# Create your views here.

def index(request):
    return HttpResponse("comment index")


def post(request):
    print("POST COMMENT")
    myDict = dict(request.POST.iterlists())
    print myDict['comment'][0].encode('utf-8')
    print myDict['taste'][0].encode('utf-8')
    print myDict['mood'][0].encode('utf-8')
    print myDict['price'][0].encode('utf-8')
    print myDict['coffeeid'][0].encode('utf-8')

    return HttpResponse("POST POST")