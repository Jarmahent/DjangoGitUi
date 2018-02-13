from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from requests import get
from json import loads


client_id = "4165edd6278ca654d60b"
client_secret = "c612a965668f90ccabbe98d0f1086eea75c66676"

def getUserInfo(user):
    data_request = get('https://api.github.com/users/{}?client_id={}&client_secret={}'.format(user, client_id, client_secret)).content.decode('utf-8')
    user_data = loads(data_request)
    print(user_data)
    return user_data


#You were creating a submission for to get the username as ajax POST


def index(request):
    #template = loader.get_template("ui/index.html")
    return render(request, "ui/index.html", getUserInfo("mstraughan86"))

def getuser(request):
    if request.method == 'POST':
        unparsed_json = request.body.decode('utf-8')
        username = loads(unparsed_json)
        print(username['gitusername'])
        return render(request, "ui/index.html", getUserInfo("jarmahent"))
    else:
        return HttpResponse("Bad.")
