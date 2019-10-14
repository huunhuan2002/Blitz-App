from flask import request
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'about' : 'hello world'}
    def post(self):
        someJson = request.get_json()
        return {'you sent' : someJson}, 201