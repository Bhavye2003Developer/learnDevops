from django.shortcuts import render
from django.http import HttpResponse
import redis

client = redis.Redis(host="redis-server", port=6379, decode_responses=True)
client.set("visits", 0)


# Create your views here.
def index(request):
    client.incr("visits")
    return HttpResponse(f"Number of visits is {client.get('visits')}")