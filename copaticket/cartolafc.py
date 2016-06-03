import requests
import json
from settings import *

url_api = 'https://api.cartolafc.globo.com'
url_auth = 'https://login.globo.com/api/authentication'


def get_league():
    """Obtem os dados da liga."""
    url = "{0}/auth/liga/{1}".format(url_api, CARTOLAFC_LIGA)
    headers = {
        'content-type': 'application/json',
        'X-GLB-Token': get_token()
    }
    resp = requests.get(url, headers=headers)
    return json.loads(resp.text)


def get_team(team_slug):
    """Obtem os dados do time"""
    url = "{0}/time/{1}".format(url_api, team_slug)
    resp = requests.get(url, headers={'content-type': 'application/json'})
    return json.loads(resp.text)


def get_game():
    """Obtem os dados da rodada"""
    url = "{0}/partidas".format(url_api)
    resp = requests.get(url, headers={'content-type': 'application/json'})
    return json.loads(resp.text)


def get_token():
    """
    Obtem o token de acesso.
    O recurso /auth/liga do cartolaFC precisa de um token para acesso"""
    data = {
        'payload': {
            'email': CARTOLAFC_EMAIL,
            'password': CARTOLAFC_PASSWORD,
            'serviceId': CARTOLAFC_SID
        }}
    headers = {'content-type': 'application/json'}
    resp = requests.post(url_auth, data=json.dumps(data), headers=headers)
    result = json.loads(resp.text)
    return result['glbId']
