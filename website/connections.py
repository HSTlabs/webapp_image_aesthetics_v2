import sqlite3
from flask import g
from . import IMG_DB_PATH, USER_DB_PATH


# One connection per request context, closed on teardown
def get_img_db():
    if 'img_db' not in g:
        g.img_db = sqlite3.connect(IMG_DB_PATH)
    return g.img_db


def get_user_db():
    if 'user_db' not in g:
        g.user_db = sqlite3.connect(USER_DB_PATH)
    return g.user_db


def close_connections(exception=None):
    for name in ('img_db', 'user_db'):
        conn = g.pop(name, None)
        if conn is not None:
            conn.close()
