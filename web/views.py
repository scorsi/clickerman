from django.http import HttpResponse
from django.template import loader

from .models import User


def index(request):
    users = User.objects.all()
    template = loader.get_template('web/index.html')
    context = {
        'users': users
    }
    return HttpResponse(template.render(context, request))
