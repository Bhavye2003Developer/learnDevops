from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.method == "POST":
        number = request.POST["number"]
        # print(number)
        f = open('DataVolume/number.txt', 'w')
        f.write(number)
        f.close()
        return redirect("home")
    return render(request, "home/home.html")