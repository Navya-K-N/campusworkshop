"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch134ajh4hstbhh7g5v0-a.oregon-postgres.render.com",
        database="todo_u1nz",
        user="root",
        password="NBkhmchnFxURMMBgCo6gb2nCWoWoIk5j")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
