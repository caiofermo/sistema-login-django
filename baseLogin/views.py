from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Função para renderizar a página inicial protegida por login
@login_required
def home(request):
    return render(request, 'home.html')     


# Função para renderizar o formulário de registro que ja vem no django
def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect ('login') # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    return render (request, 'registration/signup.html', {"form": form })


# Função para logout
def logout_view(request):
    logout(request)
    return render(request, 'registration/login.htm')
