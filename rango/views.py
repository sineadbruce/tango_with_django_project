from django.shortcuts import render

from django.http import HttpResponse

def index(request): # this is a view called index - views take one argument:
                    # a HttpResponse object called "request".
                    # Said object takes string param representing content of page
    return HttpResponse(
        "Rango says hey there partner! <br>"
        "<a href = 'http://127.0.0.1:8000/rango/about/'>About Page</a>"
        )

def about(request):
    return HttpResponse(
        "<a href = 'http://127.0.0.1:8000/'>Home</a> <br>"
        "Rango says here is the about page."
        )
