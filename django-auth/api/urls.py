from api.views import UserRegisterView, UserLoginView, UserAuthView
from django.urls import path

urlpatterns = [
    path("users/auth/", UserAuthView.as_view()),
    path("users/login/", UserLoginView.as_view()),
    path("users/register/", UserRegisterView.as_view()),
]
