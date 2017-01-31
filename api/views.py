from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from web.models import Bundle, Score
import random
import json


def get_bundle_leaderboard(bundle):
    leaderboard = Score.objects.order_by("-highscore").filter(bundle=bundle)[:10]
    response_data = {}
    i = 0
    for highscore in leaderboard:
        response_data[i] = {
            "name": highscore.user.username,
            "score": highscore.highscore
        }
        i += 1
    return response_data


def get_bundle_position(bundle, scoreObj):
    scores = Score.objects.order_by("-highscore").filter(bundle=bundle)
    i = 0
    for score in scores:
        if score == scoreObj:
            return str(i)
        i += 1
    return str(i)


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
        if score.regeneration_date + timedelta(hours=1) < timezone.now():
            score.regeneration_date = timezone.now()
            score.remaining_clicks = 100
        elif score.remaining_clicks <= 0:
            response_data = {
                "leaderboard": get_bundle_leaderboard(bundle),
                "personal": {
                    "score": "none",
                    "highscore": score.highscore,
                    "position": get_bundle_position(bundle, score),
                    "nb_clicks": score.clicks,
                    "last_clicks": 0
                },
                "error": "no_last_clicks"
            }
            return HttpResponse(json.dumps(response_data))
        value = random.randint(0, 1000000)
        if value > score.highscore:
            score.highscore = value
        score.clicks += 1
        score.remaining_clicks -= 1
        score.save()
        response_data = {
            "leaderboard": get_bundle_leaderboard(bundle),
            "personal": {
                "score": value,
                "highscore": score.highscore,
                "position": get_bundle_position(bundle, score),
                "nb_clicks": score.clicks,
                "last_clicks": score.remaining_clicks
            }
        }
        return HttpResponse(json.dumps(response_data))
    else:
        return HttpResponse('{"error": "user_is_not_authenticated"}')
