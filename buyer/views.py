from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from django.contrib.auth.models import User
from . import forms
from car_app.models import Order
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



# Create your views here.

class RegisterView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Registered successfully')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login information incorrect')
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logged out successfully')
        return super().dispatch(request, *args, **kwargs)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.UserChangeDataForm(
            request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Account updated successfully")
            return redirect('profile')
    else:
        profile_form = forms.UserChangeDataForm(
            instance=request.user)  # Prepopulate form with user data

    return render(request, 'updateProfile.html', {'form': profile_form, 'type': 'Change Data'})

@login_required
def pass_change(request):
    if request.method == 'POST':
        pass_form = forms.PasswordChangeForm(request.user, request.POST)
        if pass_form.is_valid():
            user = pass_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        pass_form = forms.PasswordChangeForm(request.user)
    return render(request, 'changePassword.html', {'form': pass_form})


@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})