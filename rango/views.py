from django.shortcuts import render

from django.http import HttpResponse

def index(request): # this is a view called index - views take one argument:
                    # a HttpResponse object called "request".
                    # Said object takes string param representing content of page
    return HttpResponse("Rango says hey there partner!")
