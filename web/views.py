from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import User

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('OK!')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'register_form': form})
