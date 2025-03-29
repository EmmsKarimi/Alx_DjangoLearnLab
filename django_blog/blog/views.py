from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

def home(request):
    return render(request, 'blog/home.html')

@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")  # Refresh page after saving
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})
