
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse

from account.forms import RegisterForm, LoginForm, UserForm, ProfileForm, AddressForm
from .models import Profile


def home(request):
    return TemplateResponse(request, 'home.html')


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
