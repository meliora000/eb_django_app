from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader,Context
import json
from .forms import LoginFrom,SignUpForm
from .models import USER
from django.db import models
# Create your views here.

def signUp(request):
    form = SignUpForm

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['signup_name']
            email = form.cleaned_data['signup_email']
            id = form.cleaned_data['signup_id']
            password = form.cleaned_data['signup_password']
            str = name + "<>" + email + "<>" + id + "<>" + password + "<>"
            print str

    return render(request,"users/signup.html",{'form':form})

def login(request):
    print 'user login'
    request.session['loginstatus'] = "needlogin"

    user = {}

    user['status'] = "NONE"
    user['id'] = "NONE"
    user['password'] = "NONE"



    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            inputId = form.cleaned_data['login_id']
            inputPass = int(form.cleaned_data['login_password'])

            try:
                foo = USER.objects.get(userid = inputId)
                userPass = int(foo.userpassword)

                if inputPass == userPass:
                    print 'login'
                    user['id'] = foo.userid
                    user['password'] = foo.name
                    user['userName'] = foo.name
                    user['status'] = 'login'

                    request.session['loginstatus'] = "login"
                    request.session['username'] = foo.name
                    request.session['userid'] = foo.userid


                else:
                    print 'password'
                    user['id'] = "password"
                    user['password'] = "different"
                    user['status'] = 'password'


            except USER.DoesNotExist:
                print 'No ID'
                user['id'] = "notexist"
                user['password'] = "id"

    return HttpResponse(json.dumps({'message':user}),content_type="application/json")

def status(request):
    print 'get'
    info = {}
    info['status'] = request.session['loginstatus']
    info['name'] = request.session['username']
    info['id'] = request.session['userid']
    return HttpResponse(json.dumps({'login':info}),content_type="application/json")

def logout(request):
    request.session['loginstatus'] = "none"
    request.session['username'] = "none"
    request.session['userid'] = "none"
    return HttpResponse("LOGOUT")