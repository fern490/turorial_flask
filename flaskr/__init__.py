from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "<p>Hello, World!</p>"
