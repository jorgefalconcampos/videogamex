from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.decorators import login_required


def base(request):
    template = 'vgmxApp/site/base.html'
    if request.method == 'GET':
        return redirect('index')
    return render(request, template)


def index(request):
    template = 'vgmxApp/site/index.html'
    return render(request, template)


def login(request):
    template = 'vgmxApp/staff/login.html'
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
    template = 'vgmxApp/staff/dashboard.html'
    return render (request, template)


def logout(request):
    do_logout(request)
    return redirect('index')