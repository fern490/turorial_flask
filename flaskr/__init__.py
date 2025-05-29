from flask import Flask, url_for, render_template, request, redirect, flash, session
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'dev'  # Necesario para sesiones y mensajes flash

# Base de datos
def get_db():
    conn = sqlite3.connect('datos.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

# Rutas
@app.route('/')
def index():
    user = session.get('user_id')
    return f'index - logueado como: {user}' if user else 'index - no logueado'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# Funciones auxiliares
def do_the_login():
    username = request.form['username']
    password = request.form['password']

    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    error = None
    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return redirect(url_for('index'))

    flash(error)
    return redirect(url_for('login'))

def show_the_login_form():
    return render_template('login.html')

# Debug print
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
