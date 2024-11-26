from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm

# Index View (Optional, replace if unused)
def index(request):
    return render(request, 'accounts/index.html')

# Login View
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomAuthenticationForm

# Dashboard (Authenticated User Home)
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'username': request.user.username})

# Sign-Up View
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Password Change View
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_change_done')

# Profile View
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Logout View
def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
