from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader,Context
from .models import Object

def index(request):
    if request.method == 'POST':
        print 'HOME: POST'

        #Saved Address
        request.session['address'] = request.POST['address']
        return HttpResponseRedirect('/search/')

    return render(request,"home.html")

def search(request):
    print 'SEARCH'
    t = loader.get_template('search.html')
    try:
        address =  request.session['address']
    except KeyError:
         return HttpResponseRedirect('../')

    address = address.split(",")
    add = " ".join(address[:-2])
    lat = float(address[-2])
    lng = float(address[-1])
    fulladdress = "{0},{1},{2}".format(add,lat,lng)
    dis = .003
    MINlat = lat - dis
    MAXlat = lat + dis
    MINlng = lng - dis
    MAXlng = lng + dis

    qs = Object.objects.filter(lat__gt =MINlat, lat__lt = MAXlat,lng__gt=MINlng,lng__lt=MAXlng)
    x = 0
    info = []
    memo = []


    for i in qs:
        data = {}
        data['name'] = i.name
        data['lat'] = str(i.lat)
        data['lng'] = str(i.lng)
        data['address'] = i.add
        info.append(data)
        fullinfo = i.name+"-"+str(i.lat - .00011)+"-"+str(i.lng + .00005)
        memo.append(fullinfo)
    memo = ",".join(memo)
    info = {'info':info,'memo':memo,"address":fulladdress}

    return render(request,'search.html',info)

def map(request):
    return HttpResponse("test for daum map")
