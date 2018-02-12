from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from requests import get
from json import loads


client_id = ""
client_secret = ""

def getUserInfo(user):
    data_request = get('https://api.github.com/users/{}?client_id={}&client_secret={}'.format(user, client_id, client_secret)).content.decode('utf-8')
    user_data = loads(data_request)
    return user_data


#You were creating a submission for to get the username as ajax POST


def index(request):
    #template = loader.get_template("ui/index.html")
    return render(request, "ui/index.html", getUserInfo("mstraughan86"))

def getuser(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("Good!")
    else:
        return HttpResponse("Bad.")
