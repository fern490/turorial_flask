from flask import Flask, url_for, render_template, request, redirect

import sqlite3

app = Flask(__name__)

def abrirConexion():
    conexion = sqlite3.connect("datos.sqlite")
    conexion.row_factory = sqlite3.Row
    return conexion

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

@app.route("/")
def hola_mundo():
    return "<p>Hello, World!</p>"

