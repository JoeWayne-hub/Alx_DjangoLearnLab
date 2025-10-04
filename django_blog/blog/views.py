from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages

def register_view(request):
    """
    Handle user registration. On POST with valid form create user and log them in.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in immediately
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {"form": form})


@login_required
def profile_view(request):
    """
    Display profile details; allow POST to edit profile.
    """
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {"form": form, "profile": profile})
