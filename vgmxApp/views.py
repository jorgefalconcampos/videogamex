import os
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required


VGMX_APP_FOLDER_NAME = 'vgmxApp'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TPS stands for: templates folder path
TFP_SITE =  os.path.join(BASE_DIR, VGMX_APP_FOLDER_NAME, "templates", VGMX_APP_FOLDER_NAME, "site")
TFP_STAFF =  os.path.join(BASE_DIR, VGMX_APP_FOLDER_NAME, "templates", VGMX_APP_FOLDER_NAME, "staff")


def base(request):
    if request.method == 'GET':
        return redirect('index')
    return render(request)


def index(request):
    template = os.path.join(TFP_SITE, 'index.html')
    return render(request, template)


def login(request):
    template = os.path.join(TFP_STAFF, 'login.html')
    if request.user.is_authenticated:
        # print("The user is authenticated")
        return redirect('dashboard')
    else:
        if request.POST.get('action') == 'login_Form':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if (username and password):
                user = authenticate(request, username=username, password=password)
                if user is not None and user.is_active:
                    do_login(request, user)
                    return JsonResponse({'status': True})
                else:
                    return JsonResponse({'status': False, 'err_code': 'login_failed'})
            else:
                return JsonResponse({'status': False, 'err_code': 'invalid_form'})
    context = {}
    return render(request, template, context)


@login_required(login_url='login')
def dashboard(request):
    template = os.path.join(TFP_STAFF, 'dashboard.html')    
    return render (request, template)


def logout(request):
    do_logout(request)
    return redirect('index')


def efectivo(request):
    template = os.path.join(TFP_SITE, 'efectivo.html')
    return render (request, template)


def metodos_de_pago(request):
    template = os.path.join(TFP_SITE, 'metodos_pago.html')
    return render (request, template)


def productos(request):
    template = os.path.join(TFP_SITE, 'productos.html')
    return render (request, template)

def tarjeta(request):
    template = os.path.join(TFP_SITE, 'tarjeta.html')
    return render (request, template)





