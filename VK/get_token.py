from urllib.parse import urlencode


def get_token_link():
    APP_ID = 7977628
    #SERV_TOKEN = 'c9a04146c9a04146c9a0414674c9d9fbdacc9a0c9a04146a8cbbcfcb44951d5f2c14c43'
    VER = 5.103

    OAUTH_URL = 'https://oauth.vk.com/authorize'
    OAUTH_PARAMS = {
        'client_id': APP_ID,
        'display': 'page',
        'scope': 'offline',
        'response_type': 'token',
        'v': VER
    }

    return ('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))