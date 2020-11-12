import ujson
from django.http.response import HttpResponse
from django.shortcuts import render

def about(request):
    context = {
        'text': 'test text'
    }
    return render(request, 'about.html', context=context)