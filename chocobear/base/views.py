from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.template import loader

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