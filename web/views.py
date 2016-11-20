from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm


@login_required(login_url='login/')
def home(request):
    return TemplateResponse(request, 'home.html')


def auth(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        login_form = LoginForm(request, data=request.POST)

        action = request.POST.get('action', '')
        if action == 'register' and register_form.is_valid():
            register_form.save()
            return HttpResponse('Register OK!')
        elif action == 'login' and login_form.is_valid():
            login(request, login_form.get_user())
            return HttpResponse('Login: OK!')

        context = {
            'register_form': register_form,
            'login_form': login_form,
        }
    else:
        context = {
            'register_form': RegisterForm(),
            'login_form': LoginForm(),
        }
    return TemplateResponse(request, 'register.html', context)
