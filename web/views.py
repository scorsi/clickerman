from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template.response import TemplateResponse
from account.forms import AddressForm
from web.models import Bundle


def home_enterprise(request):
    return HttpResponse('home_enterprise')


def home_clicker(request):
    bundles = Bundle.objects.filter(status='2')
    return TemplateResponse(request, 'home/clicker.html', {'bundles': bundles})


def home(request):
    if request.user.is_authenticated:
        if request.user.profile.enterprise is not None:
            return home_enterprise(request)
        else:
            return home_clicker(request)
    return TemplateResponse(request, 'home/visitor.html')


def bundle(request, bundle_id):
    try:
        bundle_obj = Bundle.objects.filter(status='2').get(id=bundle_id)
    except ObjectDoesNotExist:
        return HttpResponse('404')
    return TemplateResponse(request, 'bundle.html',{'bundle': bundle_obj})


def construction(request):
    return TemplateResponse(request, 'construction.html')


def accueil(request):
    if request.user.is_authenticated():
        """Check if user is an enterprise or a normal user"""
        return HttpResponse('User login page not finished')
    return TemplateResponse(request, 'accueil.html')


@login_required(login_url='/account/login/')
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
