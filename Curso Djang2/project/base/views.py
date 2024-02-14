from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

from .models import Post, Comment

def loginPage(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente')
                return redirect('/')
        messages.error(request, 'Datos incorrectos')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')

def register(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no son iguales')
            return redirect('/registro')
        User.objects.create_user(username, email=email, first_name=first_name, last_name=last_name, password=password)
    return render(request, 'registro.html')

def home(request):
    posts = Post.objects.order_by("created")
    return render(request, 'home.html', { 'posts': posts })

def post(request, id = None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if (id is None):
            Post.objects.create(
                title = request.POST.get('title'),
                text = request.POST.get('text'),
                user = request.user
            )
            messages.success(request, 'Se creó el post correctamente')
            return redirect('/')
        else:
            p = Post.objects.get(id = id)
            if (p.user == request.user):
                p.title = request.objects.get('title')
                p.text = request.objects.get('text')
                p.save()
    context = {}
    if id is not None:
        p = Post.objects.get(id =id)
        context['post'] = p
    return render(request, 'ejemplo.html', context)

def registerPage(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')
        User.objects.create_user(username, email = email, first_name = first_name, last_name = last_name, password = password)
        return redirect('/login')
    return render(request, 'registro.html')

def comment(request):
    p = Post.objects.get(id=request.POST.get('post'))
    Comment.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        post = p
    )
    return redirect('/')