from flask import Flask
from flask_restful import Api
from controller import Authenticate, Webhook

app = Flask(__name__)
api = Api(app)

api.add_resource(Authenticate.Authenticate, '/auth')
api.add_resource(Webhook.WebHook, '/webhook')

if __name__ == '__main__':
    app.run(debug=True)
