from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, "Account was created for " + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('posts')
    else:
        if request.method == 'POST':
            # print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')  
            print(username)
            print(password)   

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('posts')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'account/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('posts')


def dummy_page(request):
    return render(request, "account/dummy_index.html")

def index(request):
    context = {}
    return render(request, "location/index.html", context)
