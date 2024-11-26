from django.urls import path
from .views import (
    UserLoginView,
    dashboard,
    signup_view,
    UserPasswordChangeView,
    profile_view,
    custom_logout_view,
)
from django.contrib.auth import views as auth_views

# URL patterns for authentication and user management
urlpatterns = [
    # Home and Dashboard
    path('', dashboard, name='dashboard'),  # Default home route
    path('dashboard/', dashboard, name='dashboard'),  # Explicit dashboard route

    # Authentication
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),

    # Password Management
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done',
    ),

    # Profile
    path('profile/', profile_view, name='profile'),
]
