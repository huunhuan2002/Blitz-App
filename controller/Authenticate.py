from flask import request, redirect
from flask_restful import Resource
from datetime import datetime
from urllib.parse import quote_plus
from rauth import OAuth2Service
import os
import json

class Authenticate(Resource):
    def get(self):
        urlAuthorize = os.environ['URL_AUTHORIZE']
        appId = os.environ['APP_ID']
        scope =  quote_plus(os.environ['SCOPE'])
        redirectUrl = quote_plus(str(os.environ['HOST_NAME']) + '/auth')
        nonce = datetime.timestamp(datetime.now())
        responseMode = quote_plus("form_post")
        responseType = quote_plus("code id_token")

        loginUrl = str(urlAuthorize) + "?response_mode={}&response_type={}&scope={}&client_id={}&redirect_uri={}&nonce={}"
        loginUrl = loginUrl.format(responseMode, responseType, scope, appId, redirectUrl, nonce)

        return redirect(loginUrl)

    def post(self):
        appId = os.environ['APP_ID']
        appSecret = os.environ['APP_SECRET']
        grantType = os.environ['GRANT_TYPE']
        urlAuthorize = os.environ['URL_AUTHORIZE']
        urlConnectToken = os.environ['URL_CONNECT_TOKEN']
        code = request.form['code']
        redirectUrl = str(os.environ['HOST_NAME']) + '/auth'

        oauthService = OAuth2Service(
            client_id = appId,
            client_secret = appSecret,
            name = '',
            authorize_url = urlAuthorize,
            access_token_url = urlConnectToken,
            base_url = ''
        )

        params = {
            'code' : code,
            "grant_type": grantType,
            "redirect_uri": redirectUrl
        }

        result = oauthService.get_raw_access_token(data = params)
        return result.json()

class AuthenticateCallback(Resource):
    def post(self):
        return request.form
