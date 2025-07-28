from django.http import HttpResponse
from django.shortcuts import render


def test1(request):
    return HttpResponse("salam bar shoma! avvalin view!")
