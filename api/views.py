import http

from django.http import JsonResponse
from num2words import num2words
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(["GET", "POST"])
def number(request):
    data, parsed, status_phrase = {}, None, ''
    data = get_data(request)
    if _validate(data):
        status_phrase = "OK"
        parsed = parse_num(data)
    if not parsed:
        status_phrase = "BAD_REQUEST"
        result = output(status_phrase)
    else:
        result = output(status_phrase, parsed)
    return JsonResponse(result, status=http.HTTPStatus[status_phrase].value)


def _validate(num: int) -> bool:
    valid = False
    try:
        if type(num) is int or int(num):
            valid = True
        elif type(num) is dict and type(num['number']) is int:
            valid = True
    except (TypeError, ValueError):
        pass
    finally:
        return valid


def get_data(request):
    data = {}
    if request.method == 'GET':
        data = request.query_params.get('number', None)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if type(data) is dict and dict['number']:
            data = data['number']
    return data


def parse_num(num: int) -> str:
    return num2words(num)


def output(status_phrase, *argv):
    result = {'reason_phrase': http.HTTPStatus[status_phrase].phrase}
    if argv:
        result.update({'num_in_english': argv[0]})
    return result
