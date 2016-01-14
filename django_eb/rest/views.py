from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from search.models import Object
from comment.models import Comment
# Create your views here.

def index(request,lat,lng):
    lat = float(lat)
    lng = float(lng)
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
            print i.add
            data['daummap'] = "http://map.daum.net/link/to/" + "_".join(i.name.split(" ")) + "," + data['lat'] + "," + data['lng']
            data['coffeeId'] = str(i.id)
            data['comments'] = []
            for j in Comment.objects.filter(coffee = coffeeid):
                commentdata = {}
                commentdata['userID'] = j.user_id
                commentdata['comment'] = j.comment
                data['comments'].append(commentdata)

            info.append(data)

    info = {'info':info}

    return HttpResponse(json.dumps({'SEARCH':info},ensure_ascii=False),content_type="application/json; charset=utf-8")