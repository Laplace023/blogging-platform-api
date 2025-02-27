import sqlite3
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

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
        abort(404, message="does not exist")

validateEntry(3)


