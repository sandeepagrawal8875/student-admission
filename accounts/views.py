from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm


def signup(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                
    return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')