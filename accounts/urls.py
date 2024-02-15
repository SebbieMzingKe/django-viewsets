from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.SignUPView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name = "login")

]