import http

from django.http import JsonResponse, HttpResponse
from num2words import num2words
from rest_framework.decorators import api_view


@api_view(["POST"])
def number(request):
    parsed, num, status_code = None, request.data['number'], "BAD_REQUEST"
    if validate(num):
        status_code = "OK"
        parsed = parse_int(num)
    if not parsed:
        result = output(status_code)
    else:
        result = output(status_code, parsed)
    return JsonResponse(result)


def validate(num: int) -> int:
    return type(num) is int


def parse_int(num: int) -> str:
    result = num2words(num)
    return result


def parse_status(status):
    return str(http.HTTPStatus[status].value) + ' ' + http.HTTPStatus[status].phrase


def output(status, *argv):
    result = {'status': parse_status(status)}
    if argv:
        result.update({'num_to_english': argv[0]})
    return result
