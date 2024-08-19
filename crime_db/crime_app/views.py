from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Criminal
from .forms import CriminalForm, SearchForm
from django.db import models
from allauth.account.views import LoginView
from allauth.account.views import SignupView

class CustomLoginView(LoginView):
    template_name = 'login.html'
class CustomSignUpView(SignupView):
    template_name = 'signup.html'
@login_required
def home(request):
    criminals = Criminal.objects.all()
    return render(request, 'home.html', {'criminals': criminals})

@login_required
def add_criminal(request):
    if request.method == 'POST':
        form = CriminalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CriminalForm()
    return render(request, 'add_criminal.html', {'form': form})

@login_required
def search_criminal(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            criminals = Criminal.objects.filter(
                models.Q(name__icontains=search_term) | 
                models.Q(crime__icontains=search_term)
            )
            return render(request, 'search_results.html', {'criminals': criminals})
    else:
        form = SearchForm()
    return render(request, 'search_results.html', {'form': form})

@login_required
def criminal_details(request, criminal_id):
    criminal = Criminal.objects.get(pk=criminal_id)
    return render(request, 'criminal_details.html', {'criminal': criminal})