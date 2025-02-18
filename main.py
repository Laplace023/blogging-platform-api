#!/usr/bin/env python3

#adding the libraries
from flask import Flask, request
from flask_restful import Resource, Api #base modules for API
from flask_restful import fields, marshal_with #data formatting
import mysql.connector

app = Flask(__name__)
api = Api(app)

#defining the blog structure
blogFields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'category': fields.String,
    'tags': fields.List,
    'createdAt': fields.String,
    'updatedAt': fields.String,
}

class blog(Resource):
    def get(self, blogID):
        pass
    def delete(self, blogID):
        pass
    def put(self, blogID):
        pass

    