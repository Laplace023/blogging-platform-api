#!/usr/bin/env python3

#INFO: adding the libraries
import os
from flask import Flask, request
from flask_restful import Resource, Api #NOTE: base modules for API
from flask_restful import fields, marshal_with, reqparse, abort #NOTE: data formatting
import sqlite3

from utils import createDbTable, generateTimeNow,generateId

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
parse.add_argument('content', location='form')
parse.add_argument('title', location='form')
parse.add_argument('category', location='form')
parse.add_argument('tags', location='form')

#INFO: Entry validation,404, function
def validateEntry(blogID):
    conn = sqlite3.connect('blogs.db')
    cursor = conn.cursor()
    #NOTE: Query
    data = cursor.execute("""
        SELECT DISTINCT id
        FROM posts
        """).fetchall()
    listData = [x[0] for x in data]

    if str(blogID) not in listData:
        abort(http_status_code=404, message="does not exist")

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
        validateEntry(blogID)
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
        validateEntry(blogID)
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
        validateEntry(blogID)
        updatedAt = generateTimeNow.timeNow()
        args = parse.parse_args()
        content = args['content'] #NOTE: fetches from title e.g. -d title=<data_given>
        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        #NOTE: Query
        cursor.execute(f"""
            UPDATE posts
            set content='{content}', updatedAt='{updatedAt}'
            WHERE id='{blogID}'
        """)
        conn.commit()
        data = cursor.execute(f"""
            SELECT * FROM posts 
            WHERE id='{blogID}'
        """).fetchall()
        dataDict = dict(zip([c[0] for c in cursor.description], data[0]))
        conn.close()
        return dataDict, 201

#TODO: Add a create function
class blogCreate(Resource):
    def post(self):
        #TODO: create the sql query
        args = parse.parse_args()
        title = args['title']
        content = args['content']
        category = args['category']
        tags = args['tags']
        id = generateId.id()
        createdAt = generateTimeNow.timeNow()
        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        #NOTE: Query
        cursor.execute(f"""
        INSERT INTO posts
        VALUES ('{id}', '{title}', '{content}', '{category}', '{tags}', '{createdAt}', 'N/A')
        """)
        conn.commit()
        data = cursor.execute(f"""
            SELECT * FROM posts 
            WHERE id='{id}'
        """).fetchall()
        dataDict = dict(zip([c[0] for c in cursor.description], data[0]))
        conn.close()

        return dataDict, 202

api.add_resource(blog, '/blogs/<blogID>')
api.add_resource(blogCreate, '/blogs')

#INFO: Debugger
if __name__ == '__main__':
    app.run(debug=True)