from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader,Context
from django.db import IntegrityError
import json
import simplejson
from models import Favorite
from search.models import Object
from users.models import USER
# Create your views here.

def index(request):
    userID = request.session['userid']
    user = Favorite.objects.filter(user=userID)
    info = []
    for i in user:
        data = {}
        data['name'] =  i.coffee.name
        data['add'] = i.coffee.add
        info.append(data)
    return render(request,"fav/favorite.html",{'info':info})

def fpost(request):
    print 'fpost'
    if(request.session['userid'] == 'none'):
        return HttpResponse(json.dumps({'message':'Login First' }),content_type="application/json")

    myDict = dict(request.POST.iterlists())
    coffeeID = myDict["hello"][0].encode('utf-8')
    userID = request.session['userid']
    #check if user already added
        #ifnot add
    print coffeeID
    print userID

    c = Object.objects.get(id = int(coffeeID))
    u = USER.objects.get(userid = userID)
    try:
        f = Favorite.objects.create(coffee = c,user =u)
        message = "successfullyadded"
    except IntegrityError as e:
        message = "alreadyExist"

    return HttpResponse(json.dumps({'message':message }),content_type="application/json")