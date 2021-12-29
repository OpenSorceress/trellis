from django.shortcuts import render
from num2words import num2words
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def number(request):
    if request.method == 'POST':
        result = num2words(request.query_params['number'])
        return JsonResponse({"message": result})
    return JsonResponse({"message": "400 BAD REQUEST"})
