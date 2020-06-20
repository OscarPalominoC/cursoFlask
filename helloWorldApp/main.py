from flask import Flask, request, make_response, redirect, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return render_template('hello.html', user_ip = user_ip)

TODOS = ['To do 1', 'To do 2', 'To do 3']

@app.route('/control-structure')
def control():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('control-structure.html', **context)


@app.route('/templates-inheritance')
def templates():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('templates-inheritance.html', **context)


@app.route('/static')
def statics():
    user_ip = request.cookies.get('user_ip')
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