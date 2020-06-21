from flask import Flask, request, make_response, redirect, render_template, abort, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

TODOS = ['To do 1', 'To do 2', 'To do 3']

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    return render_template('hello.html', user_ip = user_ip)


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