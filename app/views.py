from django.shortcuts import redirect, render
from django.views import View
from .models import *


from django.contrib.auth import authenticate, login, logout



class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
    def post(self, request):
        logout(request)
        return redirect('login')

class IndexView(View):
    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, 'index.html', {'produtos': produtos})
    
    def post(self, request):
        return render(request, 'index.html')



