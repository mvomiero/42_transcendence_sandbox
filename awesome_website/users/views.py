# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.http import HttpResponseNotAllowed
from .forms import CustomUserForm

def dashboard(request):
    if request.user.is_authenticated:
        bio = request.user.bio
        return render(request, "users/dashboard.html", {'bio': bio})
    else:
        # Handle the case when the user is not authenticated
        return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        
def profile_update(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            print(form.cleaned_data)  # Print form data to the console for debugging
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)  # Print form errors if any
    else:
        form = CustomUserForm(instance=request.user)
    return render(request, 'users/profile_update.html', {'form': form})