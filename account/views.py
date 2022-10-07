from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from location.models import Region
from django.views.generic import CreateView, View
from django.urls import reverse_lazy


# Create your views here.


class RegisterPage(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = "account/register.html"


# def register_page(request):
#     form = CreateUserForm()
#     regions = Region.objects.all()
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('email')
#             messages.success(request, "An account was successfully created for " + user)
#             return redirect('login')
#     context = {'form': form, 'regions': regions}
#     return render(request, 'account/register.html', context)


class LoginPageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts')
        else:
            regions = Region.objects.all()
            context = {'regions': regions}
            return render(request, 'account/login.html', context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts')
        message = "Login Failed. Username or password is incorrect"
        regions = Region.objects.all()
        context = {
            "regions": regions,
            "message": message
        }
        return render(request, "account/login.html", context)


# def login_page(request):
#     regions = Region.objects.all()
#     if request.user.is_authenticated:
#         return redirect('posts')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             print(username)
#             print(password)
#
#             user = authenticate(request, username=username, password=password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('posts')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')
#         context = {'regions': regions}
#         return render(request, 'account/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('posts')


# def dummy_page(request):
#     return render(request, "account/dummy_index.html")
#
#
# def index(request):
#     context = {}
#     return render(request, "location/index.html", context)
