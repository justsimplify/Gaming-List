from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Games
from django.conf import settings


def insert_data_in_db(reader):
    for row in reader:
        Games.objects.get_or_create(title=row[0],
                                    platform=row[1],
                                    score=row[2],
                                    genre=row[3],
                                    editors_choice=row[4])


def get_data_from_db():
    return Games.objects.all()


def get_data_from_db_by_key(key, data):
    kwargs = {
        f'{key}__iexact': data
    }
    return Games.objects.filter(**kwargs)


def parse_all_objects(data):
    return [{'title': r.title,
             'platform': r.platform,
             'genre': r.genre,
             'score': r.score,
             'editors_choice': r.editors_choice} for r in data]


@csrf_exempt
def insert(request):
    try:
        reader = settings.READER
        insert_data_in_db(reader)
        return HttpResponse('Success')
    except Exception as e:
        return HttpResponse(str(e))


@csrf_exempt
def index(request):
    return JsonResponse(parse_all_objects(get_data_from_db()), safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def filter_data(request, key=None, v=None):
    return JsonResponse(parse_all_objects(get_data_from_db_by_key(key, v)), safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def get_view(request):
    return render(request, 'cgi_backend/index.html')