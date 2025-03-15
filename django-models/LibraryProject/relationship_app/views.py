from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Ensure this line is present
from django.shortcuts import render, redirect

# User Registration View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect("home")  # Redirect to homepage or dashboard
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to homepage
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# User Logout View
def logout_view(request):
    logout(request)
    return render(request, "logout.html")
