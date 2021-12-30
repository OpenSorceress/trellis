import http
from http import HTTPStatus
from typing import Dict, Union, Any

import mypy.api, api
import django.core.validators
from django.core.exceptions import BadRequest
from django.shortcuts import render
from num2words import num2words
from django.http import JsonResponse, Http404, HttpResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException

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


def output(status, *argv):
    result = {'status': http.HTTPStatus[status], 'message': HttpResponse.status_code}
    if argv:
        result.update({'num_to_english': argv[0]})
    return result


def validate(num: int) -> int:
    return type(num) is int


def parse_int(num: int) -> str:
    result = num2words(num)
    return result
