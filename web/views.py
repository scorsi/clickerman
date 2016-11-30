from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from .forms import RegisterForm, LoginForm, UserForm, ProfileForm, AddressForm
from .models import Profile


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


@login_required(login_url='login/')
def account_edit(request):
    profile_instance = Profile.objects.get_or_create(user=request.user.id)[0]
    address_object_list = request.user.profile.addresses.all()
    i = 0
    addresses = [[0 for x in range(2)] for y in range(len(address_object_list))]
    for address in address_object_list:
        addresses[i] = {
            'object': address,
            'form': AddressForm(request.POST or None, instance=address)
        }
        i += 1
    context = {
        'user_form': UserForm(request.POST or None, request.FILES or None, instance=request.user),
        'profile_form': ProfileForm(request.POST or None, request.FILES or None, instance=profile_instance),
        'addresses': addresses,
    }
    if request.method == 'POST':
        if context['user_form'].is_valid() and context['profile_form'].is_valid():
            context['user_form'].save()
            context['profile_form'].save()
    return TemplateResponse(request, 'account_edit.html', context)


@login_required(login_url='login/')
def account_address_edit(request, address_alias):
    try:
        address = request.user.profile.addresses.get(alias=address_alias)
    except ObjectDoesNotExist:
        return HttpResponse('404')
    context = {
        'address': address,
        'address_form': AddressForm(request.POST or None, instance=address),
    }
    if context['address_form'].is_valid():
        context['address_form'].save()
    return TemplateResponse(request, 'account_address_edit.html', context)
