from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

class StudentResource(Resource):
    def get(self):
        return {"student": "resource"}