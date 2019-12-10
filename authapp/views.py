from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm

# Create your views here.


# Вьюха для логина
def login_view(request):
    title = 'Вход'
    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        print('-----POST----------')
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:main'))
        else:
            login_form = ShopUserLoginForm(data=request.POST or None)
            return render(request, 'login.html', {'login_form': login_form})
    else:
        login_form = ShopUserLoginForm()
    context_list = {'title': title, 'login_form': login_form}
    return render(request, 'login.html', context_list)


# Вьюха для выхода
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))


# Вьюха для регистрации
def register_view(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context_list = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', context_list)


# Вьюха для редактирования юзера
def edit_view(request):
    title = 'Редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context_list = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', context_list)