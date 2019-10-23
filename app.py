from flask import Flask
from flask_restful import Api
from controller import Authenticate

app = Flask(__name__)
api = Api(app)

api.add_resource(Authenticate.Authenticate, '/auth')
api.add_resource(Authenticate.AuthenticateCallback, '/auth/token')

if __name__ == '__main__':
    app.run(debug=True)
