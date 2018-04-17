# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userDB

def index(request):
    return render(request, 'LogReg/index.html')

def log_reg(request):
    if request.method == "POST":
        # print ('attempt: ', request.POST['attempt'])
        print ('POST: ', request.POST)
        if request.POST['attempt'] == "register":
            request.session['attempt'] = 'register'
            response = userDB.objects.check_create(request.POST)
        elif request.POST['attempt'] == 'login':
            request.session['attempt'] = 'login'
            response = userDB.objects.check_login(request.POST)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('LogReg:index')
        else:
            request.session['user'] = {
                "first_name": response[1].first_name,
                "last_name": response[1].last_name,
                "id": response[1].id,
            }
        return redirect('Wall:wall')
    return redirect('LogReg:index')

def logout(request):
    request.session.clear()
    return redirect('LogReg:index')
# Create your views here.
