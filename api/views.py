import http

from django.http import JsonResponse
from num2words import num2words
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(["GET", "POST"])
def number(request):
    data, parsed, status = {}, None, ''
    data = get_data(request)
    if _validate(data):
        status = "OK"
        parsed = parse_num(data)
    if not parsed:
        status = "BAD_REQUEST"
        result = output(status)
    else:
        result = output(status, parsed)
    return JsonResponse(result)


def _validate(num: int) -> bool:
    valid = False
    try:
        type(num) is int or int(num)
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
    return data


def parse_num(num: int) -> str:
    return num2words(num)


def parse_status(status):
    return str(http.HTTPStatus[status].value) + ' ' + http.HTTPStatus[status].phrase


def output(status, *argv):
    result = {'status': parse_status(status)}
    if argv:
        result.update({'num_to_english': argv[0]})
    return result
