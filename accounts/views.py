from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import TemplateView


# Create your views here.

class CustomLoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    next_page = reverse_lazy("accounts:profile")
    redirect_authenticated_user = True
    redirect_field_name = "next"
    authentication_form = AuthenticationForm


class CustomLogoutView(auth_views.LogoutView): pass


class CustomPasswordChangeView(auth_views.PasswordChangeView): pass


class CustomPasswordChangeDoneView(auth_views.PasswordChangeDoneView): pass


class CustomPasswordResetView(auth_views.PasswordResetView): pass


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView): pass


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView): pass


class CustomResetDone(auth_views.PasswordResetCompleteView): pass

class CustomProfileView(TemplateView):
    template_name = "user/profile.html"

class LandingPageView(TemplateView):
    template_name = "landing_page.html"