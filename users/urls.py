from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView, LoginView
from .views import UserRegisterView


app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
