from flask import Flask
from flask_restful import Api
from controller import HelloWorld, Multi

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld.HelloWorld, '/')
api.add_resource(Multi.Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
