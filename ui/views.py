from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from requests import get
from json import loads, dumps




client_id = ""
client_secret = ""

def getUserInfo(user):
    data_request = get('https://api.github.com/users/{}?client_id={}&client_secret={}'.format(user, client_id, client_secret)).content.decode('utf-8')
    user_data = loads(data_request)
    return user_data





def index(request):
    #template = loader.get_template("ui/index.html")
    return render(request, "ui/index.html", getUserInfo("mstraughan86"))

def getuser(request):
    if request.method == 'POST':
        unparsed_json = request.body.decode('utf-8')
        postData = loads(unparsed_json)
        #print(username['gitusername'])
        return HttpResponse(dumps(getUserInfo(postData['gitusername'])), content_type="application/json")
    else:
        return HttpResponse("Bad.")


def user(request):
    return render(request, "ui/index.html", getUserInfo("mstraughan86"))
