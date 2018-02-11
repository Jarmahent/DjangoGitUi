from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from requests import get
from json import loads


def getUserInfo(user):
    data_request = get('https://api.github.com/users/{}'.format(user)).content.decode('utf-8')
    user_data = loads(data_request)
    return user_data





def index(request):
    #template = loader.get_template("ui/index.html")
    return render(request, "ui/index.html", getUserInfo("jarmahent"))
