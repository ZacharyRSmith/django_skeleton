from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')