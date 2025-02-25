#!/usr/bin/env python3

#INFO: adding the libraries
import os
from flask import Flask, request
from flask_restful import Resource, Api #NOTE: base modules for API
from flask_restful import fields, marshal_with #NOTE: data formatting
import sqlite3

from utils import createDbTable

#INFO: setup, database check/creation
databaseName = 'blogs'
tableName = 'posts'
fileCheck = os.listdir()
if 'blogs.db' in fileCheck:
    pass
else:
    createDbTable.setup(databaseName, tableName)
    print(f"Created {databaseName}.db with table {tableName}")
#DONE: Database setup

#INFO: API setup
app = Flask(__name__)
api = Api(app)

#INFO: Defining the blog structure
blogFields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'category': fields.String,
    'tags': fields.List,
    'createdAt': fields.String,
    'updatedAt': fields.String,
}
#TODO: Add the api parameters later
class blog(Resource):
    def get(self, blogID):
        #INFO: Database setup
        conn = sqlite3.connect('blogs.db')
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        #NOTE: Query
        data = cursor.execute(f"SELECT * FROM posts WHERE id='{blogID}'").fetchall()
        #NOTE: Transforming the data into dictionary
        #NOTE: This line is new to me and have to ask GPT to explain what it does
        dataDict = dict(zip([c[0] for c in cursor.description], data[0]))
        #NOTE: Result
        return dataDict
    
    def delete(self, blogID):
        pass
    def put(self, blogID):
        pass

#TODO: Add a create function
class blogCreate(Resource):
    def post(self, blogID):
        #TODO: create the sql query
        pass

api.add_resource(blog, '/blogs/<blogID>')

#INFO: Debugger
if __name__ == '__main__':
    app.run(debug=True)