from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginPageView.as_view(), name="login"),
    # path('register', views.register_page, name="register"),
    path('logout', views.logout_page, name="logout"),
    path('home', views.dummy_page, name="dummy_index"),
    path('register', views.RegisterPage.as_view(), name="register"),
]