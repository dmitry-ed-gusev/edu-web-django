from django.shortcuts import render
from django.http import HttpResponse


def autoview(request):
    response: HttpResponse = HttpResponse("You're in the Autos CRUD app!")

    return response
