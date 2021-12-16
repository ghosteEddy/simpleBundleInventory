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
        form = ItemForm(helpers.getItemById(item_id))
        template = loader.get_template('base/itemEdit.html')
        context = {'form' : form}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        result = api.editItem(request, item_id)
        if result == 0:
            return redirect('baseItemMenu')
        else:
            return HttpResponse('Something Wrong')

@login_required
def itemDelete(request, item_id):
    if request.method == 'POST':
        result = api.deleteItem(request)
        return HttpResponse(json.dumps({'result' : result}))
    return redirect('baseItemMenu')

@login_required
def bundleList(request):
    if request.method == 'GET':
        data = api.getAllBundles(request)
        template = loader.get_template('base/bundleList.html')
        context = data
        return HttpResponse(template.render(context, request))

@login_required
def bundleAdd(request):
    if request.method == 'GET':
        template = loader.get_template('base/bundleAdd.html')
        data = api.getAllItems(request)
        context = data
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        if len(request.POST) <= 3:
            return HttpResponse('please select item in bundle')
        print(request.POST)
        result = api.createBundle(request)
        if result == 0:
            return redirect('baseBundleMenu')
        else:
            return HttpResponse('Something Wrong')

@login_required
def bundleEdit(request, bundleId):
    if request.method == 'GET':
        template = loader.get_template('base/bundleEdit.html')
        data = api.getBundleInfo(bundleId)
        context = data
        context['allItems'] = api.getAllItems(request)
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        if len(request.POST) <= 3:
            return HttpResponse('please select item in bundle')
        result = api.editBundle(request)
        if result == 0:
            return redirect('baseBundleMenu')
        else:
            return HttpResponse('Something Wrong')

@login_required
def inventoryMenu(request):
    if request.method == 'GET':
        template = loader.get_template('base/inventoryList.html')
        data = api.getAllItems(request)
        context = data
        return HttpResponse(template.render(context, request))

@login_required
def updateInventory(request):
    if request.method == 'POST':
        result = api.updateInventory(request)
        return HttpResponse(json.dumps({'result' : result}))

@login_required
def inventorySellBundle(request):
    if request.method == 'POST':
        result = api.sellBundle(request)
        return HttpResponse(json.dumps({'result' : result}))

@login_required
def inventoryManual(request):
    if request.method == 'GET':
        template = loader.get_template('base/inventoryManual.html')
        data = api.getAllItems(request)
        context = data
        return HttpResponse(template.render(context, request))     

@login_required
def inventoryIn(request):
    if request.method == 'GET':
        template = loader.get_template('base/inventoryIn.html')
        data = api.getAllItems(request)
        context = data
        return HttpResponse(template.render(context, request))

@login_required
def inventoryOutShopee(request):
    if request.method == 'GET':
        template = loader.get_template('base/inventoryOutShopee.html')
        data = api.getAllBundles(request, 'SHOPEE')
        context = data
        return HttpResponse(template.render(context, request))

@login_required
def inventoryOutLazada(request):
    if request.method == 'GET':
        template = loader.get_template('base/inventoryOutLazada.html')
        data = api.getAllBundles(request, 'LAZADA')
        context = data
        return HttpResponse(template.render(context, request))