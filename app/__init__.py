"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqs8ou9tun42u4lp10-a.oregon-postgres.render.com",
        database="task_db_8ijr",
        user="task_db_8ijr_user",
        password="YKXjzu1OMkGn1IInqLS8kGoCfS7M55lM")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
