from flask import request, redirect
from flask_restful import Resource

class Authenticate(Resource):
    def get(self):
        return {'test':request.args}