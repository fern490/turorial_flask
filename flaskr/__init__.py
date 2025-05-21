from flask import Flask, url_for, render_template, request, redirect

import sqlite3

app = Flask(__name__)

def abrirConexion():
    conexion = sqlite3.connect("sakila_master.db.sqlite")
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
