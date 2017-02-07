from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from web.models import Bundle, Score
import random
import json


def generator_number():
    return int(abs(random.gauss(0, 0.1) * 1000000))


def get_bundle_leaderboard(bundle):
    leaderboard = bundle.leaderboard()
    response_data = {}
    i = 0
    for highscore in leaderboard:
        response_data[i] = {
            "name": highscore.user.username,
            "score": highscore.highscore
        }
        i += 1
    return response_data


def bundle_leaderboard(request, bundle_id):
    if request.user.is_authenticated():
        try:
            bundle = Bundle.objects.get(id=bundle_id)
        except ObjectDoesNotExist:
            return HttpResponse('{"error": "bundle_not_found"}')
        return HttpResponse(json.dumps(get_bundle_leaderboard(bundle)))
    return HttpResponse('{"error": "user_is_not_authenticated"}')


def bundle_click(request, bundle_id):
    if request.user.is_authenticated():
        try:
            bundle = Bundle.objects.get(id=bundle_id)
        except ObjectDoesNotExist:
            return HttpResponse('{"error": "bundle_not_found"}')
        try:
            score = Score.objects.get(user=request.user.id, bundle=bundle_id)
        except ObjectDoesNotExist:
            score = Score.objects.create(user=request.user, bundle=bundle)
        score.check_remaining_clicks()
        if score.remaining_clicks <= 0:
            response_data = {
                "score": "none",
                "highscore": score.highscore,
                "position": score.position(),
                "nb_clicks": score.clicks,
                "last_clicks": 0,
                "error": "no_last_clicks"
            }
            return HttpResponse(json.dumps(response_data))
        value = generator_number()
        if value > score.highscore:
            score.highscore = value
        score.clicks += 1
        score.remaining_clicks -= 1
        score.save()
        response_data = {
            "score": value,
            "highscore": score.highscore,
            "position": score.position(),
            "nb_clicks": score.clicks,
            "last_clicks": score.remaining_clicks
        }
        return HttpResponse(json.dumps(response_data))
    else:
        return HttpResponse('{"error": "user_is_not_authenticated"}')


def test_generator(request):
    return HttpResponse(str(generator_number()))
