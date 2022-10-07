from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from location.models import Region
from django.views.generic import CreateView, View
from django.urls import reverse_lazy


class RegisterPage(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = "account/register.html"


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
            return redirect('/')
        message = "Login Failed. Username or password is incorrect"
        regions = Region.objects.all()
        context = {
            "regions": regions,
            "message": message
        }
        return render(request, "account/login.html", context)


def logout_page(request):
    logout(request)
    return redirect('posts')
