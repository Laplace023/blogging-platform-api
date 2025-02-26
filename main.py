#!/usr/bin/env python3

#INFO: adding the libraries
import os
from flask import Flask, request
from flask_restful import Resource, Api #NOTE: base modules for API
from flask_restful import fields, marshal_with, reqparse #NOTE: data formatting
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

#INFO Parsing setup
parse = reqparse.RequestParser()
parse.add_argument('title', location='form')

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
        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        #NOTE: Query
        data = cursor.execute(f"""
            SELECT * FROM posts 
            WHERE id='{blogID}'
        """).fetchall()
        #NOTE: Transforming the data into dictionary
        #NOTE: This line is new to me
        dataDict = dict(zip([c[0] for c in cursor.description], data[0]))
        conn.close()
        #NOTE: Result
        return dataDict, 200
    
    
    def delete(self, blogID):
        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        #NOTE: Query
        cursor.execute(f"""
            DELETE FROM posts 
            WHERE id='{blogID}'
        """)
        conn.commit()
        conn.close()
        #NOTE: Result
        return 204
    def put(self, blogID):
        args = parse.parse_args()
        data = args['title'] #NOTE: fetches from title e.g. -d title=<data_given>
        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        #NOTE: Query
        cursor.execute(f"""
        UPDATE posts
        set title='{data}'
        WHERE id='{blogID}'
        """)
        conn.commit()
        conn.close()
        return data, 201

#TODO: Add a create function
class blogCreate(Resource):
    def post(self, blogID):
        #TODO: create the sql query
        pass

api.add_resource(blog, '/blogs/<blogID>')

#INFO: Debugger
if __name__ == '__main__':
    app.run(debug=True)