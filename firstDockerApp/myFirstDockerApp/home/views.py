from django.shortcuts import render
from django.http import HttpResponse

numberOfViews = 0
def getNumberOfViews():
    global numberOfViews
    numberOfViews += 1
    return str(numberOfViews)

# Create your views here.
def home(request):
    return HttpResponse('Number of times you have visited' + getNumberOfViews() + ' times.')