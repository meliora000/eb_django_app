from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from users.models import USER
from search.models import Object
from models import Commenta

# Create your views here.

def index(request):
    return HttpResponse("comment index")


def post(request):
    print("POST COMMENT")
    myDict = dict(request.POST.iterlists())
    if(request.session['userid'] == 'none'):
        return HttpResponse(json.dumps({'status':'needlogin' }),content_type="application/json")

    userID =  request.session["userid"]
    coffeeID = myDict['coffeeid'][0].encode('utf-8')
    tasterate =  myDict['taste'][0].encode('utf-8')
    try:
        tasterate = int(tasterate)
    except ValueError:
        tasterate = 0
    commenta = myDict['comment'][0].encode('utf-8')

    #here will be collect comment and filter based on #tag



    c = Object.objects.get(id = int(coffeeID))
    u = USER.objects.get(userid = userID)

    try:
        c = Commenta.objects.create(coffee = c,user = u, rate=tasterate, comment=commenta)
        message = "successfullyadded"
    except:
        message = "alreadyexist"

    return HttpResponse(json.dumps({'status':message,'userID':userID }),content_type="application/json")