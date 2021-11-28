from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.template import loader
from .models import *
from .forms import *
import base.helpers as helpers
import json

import base.api as api

# Create your views here.
def baseIndex(request):
    return redirect('baseLogin')

def loginView(request):
    if request.method == 'GET':
        template = loader.get_template('base/login.html')
        context = {}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            redirectTarget = request.GET.get('next')
            if type(redirectTarget) != type(None):
                return redirect(redirectTarget)
            else:
                return redirect('baseDashboard')
        else:
            return HttpResponse('Wrong Credential, Please Try Again')

def logoutView(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    if request.method == 'GET':
        template = loader.get_template('base/dashboard.html')
        context = {}
        return HttpResponse(template.render(context, request))

@login_required
def itemList(request):
    if request.method == 'GET':
        data = api.getAllItems(request)
        template = loader.get_template('base/itemList.html')
        context = data
        return HttpResponse(template.render(context, request))
    
@login_required
def itemAdd(request):
    if request.method == 'GET':
        template = loader.get_template('base/itemAdd.html')
        context = {'form' : ItemForm}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        result = api.addItem(request)
        if result == 0:
            return redirect('baseItemMenu')
        else:
            return HttpResponse('Something Wrong')

@login_required
def itemEdit(request, item_id):
    if request.method == 'GET':
        form = ItemForm()
        context = {'form' : form.edit(helpers.getItemById(item_id))}
        return HttpResponse('Edit Item {}'.format(item_id))

@login_required
def itemDelete(request, item_id):
    if request.method == 'POST':
        result = api.deleteItem(request)
        return HttpResponse(json.dumps({'result' : result}))
    return redirect('baseItemMenu')

