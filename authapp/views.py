from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

# Create your views here.
from authapp.forms import ShopUserLoginForms, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    login_form = ShopUserLoginForms(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_acive:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'logon_form': login_form
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        register_form = ShopUserRegisterForm
    context = {
        'register_form': register_form
    }
    return render(request, "authapp/register.html", context)


def edit(request):
    if request.method == 'POST':

        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'edit_form': edit_form
    }

    return render(request, 'authapp/edit.html', context)
