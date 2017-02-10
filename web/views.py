from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template.response import TemplateResponse
from web.models import Bundle, Score


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


@login_required(login_url='/account/login/')
def bundle(request, bundle_id):
    if request.user.profile.enterprise is None:
        return HttpResponse('404')
    try:
        bundle_obj = Bundle.objects.filter(status='2').get(id=bundle_id)
        score_obj = Score.objects.filter(bundle=bundle_obj).get(user=request.user)
        score_obj.check_remaining_clicks()
    except ObjectDoesNotExist:
        return HttpResponse('404')
    return TemplateResponse(request, 'bundle.html',{'bundle': bundle_obj, 'score': score_obj})


def construction(request):
    return TemplateResponse(request, 'construction.html')
