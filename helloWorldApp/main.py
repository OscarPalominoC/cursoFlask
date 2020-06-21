import unittest

from flask import Flask, request, make_response, redirect, render_template, abort, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos

app = create_app()

#TODOS = ['Comprar alimentos', 'Comprar electrodomésticas', 'Comprar cama']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():    
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = current_user.id
    context = {
        'user_ip' : user_ip, 
        'todos' : get_todos(username),
        #'login_form': login_form,
        'username': username
    }
    
    return render_template('hello.html', **context)


@app.route('/control-structure')
def control():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('control-structure.html', **context)


@app.route('/test-bootstrap')
def testBootstrap():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('test-bootstrap.html', **context)


@app.route('/templates-inheritance')
def templates():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('templates-inheritance.html', **context)


@app.route('/static')
def statics():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('statics.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error = error)


@app.route('/login-form', methods=['GET', 'POST'])
def loginForm():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con éxito.')

        return redirect(url_for('index'))

    return render_template('login-form.html', **context)
