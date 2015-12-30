from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader,Context
import json
from .forms import LoginFrom
from .models import USER
from django.db import models
# Create your views here.


def login(request):
    user = {}
    user['id'] = "login"
    user['password'] = "failed"
    print 'users login'
    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            uid = form.cleaned_data['login_id']
            upass = form.cleaned_data['login_password']
            try:
                foo = USER.objects.get(userid = uid)
                if foo.userpassword == upass:
                    user['id'] = "welcome"
                    user['password'] = foo.name
                    return HttpResponse(json.dumps({'message':user }),content_type="application/json")
                else:
                    user['id'] = "password"
                    user['password'] = "different"
                    return HttpResponse(json.dumps({'message':user }),content_type="application/json")
            except USER.DoesNotExist:
                print 'login failed'
                return HttpResponse(json.dumps({'message':user }),content_type="application/json")







            return HttpResponse(json.dumps({'message':user}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'message':user }),content_type="application/json")