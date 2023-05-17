"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7il64dadc9vltinp0-a.oregon-postgres.render.com",
        database="nqvs",
        user="nqvs_user",
        password="6dFtwTm0uSd8dO0NeYkI7ufA0IpD8yzh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
