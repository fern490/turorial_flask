from flask import Flask, url_for, render_template, request

import sqlite3

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app)

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    conexion = sqlite3.connect("datos.sqlite")
    conexion.row_factory = sqlite3.Row
    return conexion

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

@app.route("/")
def hola_mundo():
    return "<p>Hello, World!</p>"


