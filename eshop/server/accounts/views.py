# from django.shortcuts import render, HttpResponseRedirect
# from .forms import AccountUserModelForm
# from django.contrib import auth
# from django.urls import reverse
# from .forms import AccountUserRegisterForm, AccountUserEditForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import LoginForm, RegistrationForm

# def login(request):
#     title = 'вход'
#
#     login_form = AccountUserModelForm(data=request.POST)
#     if request.method == 'POST' and login_form.is_valid():
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#         if user and user.is_active:
#             auth.login(request, user)
#             return HttpResponseRedirect(reverse('index'))
#
#     content = {'title': title, 'login_form': login_form}
#     return render(request, 'accounts/login.html', content)
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
#
#
# def register(request):
#     title = 'регистрация'
#
#     if request.method == 'POST':
#         register_form = AccountUserRegisterForm(request.POST, request.FILES)
#
#         if register_form.is_valid():
#             register_form.save()
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         register_form = AccountUserRegisterForm()
#
#     content = {'title': title, 'register_form': register_form}
#
#     return render(request, 'accounts/register.html', content)
#
#
# def edit(request):
#     title = 'редактирование'
#
#     if request.method == 'POST':
#         edit_form = AccountUserEditForm(request.POST, request.FILES, instance=request.user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('auth:edit'))
#     else:
#         edit_form = AccountUserEditForm(instance=request.user)
#
#     content = {'title': title, 'edit_form': edit_form}
#
#     return render(request, 'accounts/edit.html', content)


def login_view(request):
    form = LoginForm()
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password
            )
            if user and user.is_active:
                login(request, user)
                return redirect(success_url)
    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def registration_view(request):
    form = RegistrationForm()
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            if user and user.is_active:
                login(request, user)
                return redirect(success_url)
    return render(
        request,
        'accounts/registration.html',
        {'form': form}
    )
