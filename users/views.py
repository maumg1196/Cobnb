from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import UserProfile


def signin_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                context['message'] = "Listo usuario existente y activo"
                login(request, user)
                return redirect('/')
            else:
                context['message'] = "Existe usuario pero no es activo"
        else:
            context['message'] = "No existe usuario"
    return render(request, 'signin.html', context)


def signup_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        if (username and password and email and first_name and last_name):
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            userprofile = UserProfile(user=user)
            userprofile.save()
            return redirect('/signin')
    return render(request, 'signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
