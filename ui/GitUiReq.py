from github import Github
from requests import get
from json import loads


class gitUi():
    def __init__(self):
        

    def getUserInfo(user):  #Return Dict of user info from Github
        data_request = get('https://api.github.com/users/{}'.format(user)).content.decode('utf-8')
        user_data = loads(data_request)
        return user_data
