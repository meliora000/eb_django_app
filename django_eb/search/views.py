from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader,Context
from .models import Object
from .forms import LoginFrom
import json
from comment.models import Comment

def index(request):
    if request.method == 'POST':
        print 'HOME: POST'
        #Saved Address
        if 'gotosearch' in request.POST:
            request.session['address'] = request.POST['address']
            return HttpResponseRedirect('/search/')
    form = LoginFrom
    return render(request,"search/index.html",{'form':form})

def search(request):
    print 'SEARCH'
    try:
        address =  request.session['address']
    except KeyError:
         return HttpResponseRedirect('../')

    address = address.split(",")
    add = " ".join(address[:-2])
    lat = float(address[-2])
    lng = float(address[-1])
    add="address"
    fulladdress = "{0},{1},{2}".format(add,lat,lng)

    dis = .0038
    MINlat = lat - dis
    MAXlat = lat + dis
    MINlng = lng - dis
    MAXlng = lng + dis

    qs = Object.objects.filter(lat__gt =MINlat, lat__lt = MAXlat,lng__gt=MINlng,lng__lt=MAXlng)
    x = 0
    info = []
    memo = []


    for i in qs:
        if((i.lat - lat)**2 + (i.lng - lng)**2 <= dis**2):
            coffeeid = i.id
            data = {}
            data['name'] = i.name
            data['lat'] = str(i.lat)
            data['lng'] = str(i.lng)
            data['address'] = i.add
            data['daummap'] = "http://map.daum.net/link/to/" + i.name + "," + data['lat'] + "," + data['lng']
            data['comments'] = []
            for j in Comment.objects.filter(coffee = coffeeid):
                commentdata = {}
                commentdata['userID'] = j.user_id
                commentdata['comment'] = j.comment
                data['comments'].append(commentdata)

            info.append(data)
            fullinfo = i.name+"-"+str(i.lat)+"-"+str(i.lng)
            memo.append(fullinfo)
    memo = ",".join(memo)
    info = {'info':info,'memo':memo,"address":fulladdress}

    return render(request,'search/search.html',info)

def map(request):
    return HttpResponse("test for daum map")

def login(request):
   if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            user = {}
            user['id'] = form.cleaned_data['login_id']
            user['password'] = form.cleaned_data['login_password']
            return HttpResponse(json.dumps({'message':user}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message':"loigin failed" }),content_type="application/json")
