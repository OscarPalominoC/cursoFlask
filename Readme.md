# <h1> Curso de Flask</h1>

<h2>Contenido</h2>

- <a href="#Introducción">Introducción</a>
- <a href="#cómo-funcionan-las-aplicaciones-web">¿Cómo funcionan las aplicaciones web?</a>
- <a href="#qué-es-flask">¿Qué es Flask?</a>
- <a href="#hello-world-flask">Hello World Flask</a>
- <a href="#debugging-en-flask">Debugging en Flask</a>
- <a href="#request-y-response">Request y Response</a>
- <a href="#ciclos-de-request-y-response">Ciclos de Request y Response</a>
- <a href="#templates-con-Jinja">Templates con Jinja</a>
- <a href="#estructuras-de-control">Estructuras de control</a>
- <a href="#herencia-de-templates">Herencia de templates</a>
- <a href="#include-y-links">Include y Links</a>

<h2>Introducción</h2>
<p>Conoce todo el potencial de Flask como framework web de Python, integraciones con Bootstrap, GCloud, What The Forms y más.</p>
<p>Flask es sencillo de aprender, tiene una documentación clara y práctica, es rápido a la hora de renderizar puede ser hasta tres veces más rapido que Django. También es fácil de realizar una API REST, la estructura de un proyecto es flexible y es ideal para aprender desarrollo web con un framework de Python.</p>


<h2>¿Cómo funcionan las aplicaciones web?</h2>

<p>Cuando utilizas una aplicación web puedes interactuar con ella desde una computadora hasta un dispositivo móvil, pero esto no quiere decir que consume el procesamiento de tu dispositivo. Todo lo contrario, se hace en una red de servidores.

<p>Estos servidores unen su poder de procesamiento con el fin transmitir solicitudes a todo el mundo, a su vez utilizar servidores especializados para almacenar los datos con los cuales se está trabajando, así como los datos de los demás usuarios. Como todo esto sucede sin demora alguna, parecerá que la aplicación se está ejecutando de forma nativa en tu dispositivo.

<p>El servidor procesa la información obtenida por el navegador, luego se realizan los procedimientos necesarios de acuerdo a la lógica de negocio de la aplicación para regresar la información solicitada al cliente.

<p>Ejemplo:

<p>Cuando utilizamos Google Drive el cual es una aplicación web y abrimos un documento con Google Docs, el navegador se comunica con los servidores para ver y editar el documento.
<p>A medida que vayas editando el documento, tu navegador trabajará de la mano con los servidores para asegurarse que todos los cambios se estén guardando.

<p>Ventajas:

- Muchas de las aplicaciones web que existen son gratuitas.
- Puedes acceder a tu información en cualquier momento y lugar.
- No dependes de un dispositivo en específico ya que la aplicación se encuentra almacenada en la web.


<h2>¿Qué es Flask?</h2>

<p>En esta clase el profesor Bernardo Cassina nos explica cómo podemos usar Flask para desarrollar aplicaciones web escritas en Python con este framework.
<p>Flask es un framework minimalista escrito en Python que permite crear aplicaciones web rápidamente y con un mínimo de líneas de código, busca que su infraestructura inicial sea lo más simple posible y pueda personalizarse fácilmente, puedes extender sus funcionalidades con las llamadas Flask Extensions http://flask.pocoo.org/extensions/


<h2>Hello World Flask</h2>

<p>Estos son los conceptos principales que debes entender antes de hacer un Hello World en Flask:
    virtualenv: es una herramienta para crear entornos aislados de Python.
- pip: es el instalador de paquetes para Python.
- requirements.txt: es el archivo en donde se colocará todas las dependencias a instalar en nuestra aplicación.
- FLASK_APP: es la variable para identificar el archivo donde se encuentra la aplicación.

    virtualenv venv python=python3.7
    pip3 install flask
    Para ejecutar flask en la consola hay que crear una variable de entorno:
        export FLASK_APP=<nombre de archivo>
        export FLASK_APP=main.py
    Ejecutar flask run


<h2>Debugging en Flask</h2>

<p>Debugging: es el proceso de identificar y corregir errores de programación.
Para activar el debug mode escribir lo siguiente en la consola:
    
    export FLASK_DEBUG=1
    echo $FLASK_DEBUG


<h2>Request y Response</h2>

<p>Logging: es una grabación secuencial en un archivo o en una base de datos de todos los eventos que afectan a un proceso particular.
<p>Se utiliza en muchos casos distintos, para guardar información sobre la actividad de sistemas variados.
Tal vez su uso más inmediato a nuestras actividades como desarrolladores web sería el logging de accesos al servidor web, que analizado da información del tráfico de nuestro sitio. Cualquier servidor web dispone de logs con los accesos, pero además, suelen disponer de otros logs, por ejemplo, de errores.
<p>Los sistemas operativos también suelen trabajar con logs, por ejemplo para guardar incidencias, errores, accesos de usuarios, etc.
<p>A través de el logs se puede encontrar información para detectar posibles problemas en caso de que no funcione algún sistema como debiera o se haya producido una incidencia de seguridad.

- Primero conseguimos la dirección ip del usuario. En este caso va a ser la dirección local.
    - El objeto request nos va a proveer de esta información.
         
```
from flask import Flask, request
request.remote_addr -> Retorna la ip del usuario.
```

<h2>Ciclos de Request y Response</h2>
<p>Request-Response: es uno de los métodos básicos que usan las computadoras para comunicarse entre sí, en el que la primera computadora envía una solicitud de algunos datos y la segunda responde a la solicitud.
<p>Por lo general, hay una serie de intercambios de este tipo hasta que se envía el mensaje completo.
<p>Por ejemplo: navegar por una página web es un ejemplo de comunicación de request-response.
<p>Request-response se puede ver como una llamada telefónica, en la que se llama a alguien y responde a la llamada; es decir hacemos una petición y recibimos una respuesta.

<h2>Templates con Jinja</h2>
<p>Un template es un archivo html que nos permite renderear nformación estática y dinámica. Se le pueden pasar variables que posteriormente el browser podrá renderear y el usuario podrá ver la información.
<p>Para hacer esto hay que crear el directorio templates.

```
Python
    @app.route('/hello')
    def hello():
        user_ip = request.cookies.get('user_ip')
        return render_template('hello.html', user_ip = user_ip)

hello.html
    <h1>Hello world, tu ip es {{ user_ip }}</h1>
```
Jinja puede renderear variables si, y solamente si están encerradas en llaves dobles.

<h2>Estructuras de control</h2>

<p>Iteración: es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición), así como para describir una forma específica de repetición con un estado mutable.
<p>Un ejemplo de iteración sería el siguiente:

```
{% for key, segment in segment_details.items() %}
    <tr>
        <td>{{ key }}td>
        <td>{{ segment }}td>
    <tr>
{% endfor %}  
```

En este ejemplo estamos iterando por cada segment_details.items() para mostrar los campos en una tabla {{ key }} {{ segment }} de esta forma dependiendo de cuantos segment_details.items() haya se repetirá el código.

```
main.py
    TODOS = ['To do 1', 'To do 2', 'To do 3']
    @app.route('/control-structure')
    def control():
        user_ip = request.cookies.get('user_ip')
        context = {
            'user_ip' : user_ip, 
            'todos' : TODOS
        }
        return render_template('control-structure.html', **context)

control-structure.html
    {% if user_ip %}
        <h1>Estructura de control, tu ip es {{ user_ip }}</h1>
        <ul>
            {% for todo in todos %}
            <li>{{todo}}</li>
            {% endfor %}
        </ul>
        
    {% else %}
        <a href="{{ url_for('index' )}}">Ir a inicio</a>
    {% endif %}
```


<h2>Herencia de templates</h2>

<p>Macro: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.
<p>Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.
<p>En este ejemplo nuestra macro se vería de la siguiente manera:

```
{% macro nav_link(endpoint, text) %}
    {% if request.endpoint.endswith(endpoint) %}
        <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
    {% else %}
        <li><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
    {% endif %}
{% endmacro %}
```

<p>Un ejemplo de uso de macros en Flask:

```
{% from "macros.html" import nav_link with context %}
<!DOCTYPE html>
<html lang="en">
    <head>
    {% block head %}
        <title>My application</title>
    {% endblock %}
    </head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        </ul>
    {% block body %}
    {% endblock %}
    </body>
</html>
```

Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú {{ nav_link('home', 'Home') }}.

```
python
@app.route('/templates-inheritance')
def templates():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip, 
        'todos' : TODOS
    }
    return render_template('templates-inheritance.html', **context)


base.html
    <title>
        {% block title %}Curso Flask |  {% endblock %}
    </title>
    <body>
        {% block content %} {% endblock %}
    </body>


macros.html
{% macro render_todo(todo) %}
    <li>Descripción: {{todo}}</li>
{% endmacro %}


templates-inheritance.html
{% extends 'base.html' %}
{% import 'macros.html' as macros %}
{% block title%} 
{{ super() }} Binvenido {% endblock %}

{% block content %}
    {% if user_ip %}
        <h1>Estructura de control, tu ip es {{ user_ip }}</h1>
        <ul>
            {% for todo in todos %}
                {{macros.render_todo(todo)}}
            {% endfor %}
        </ul>
    {% else %}
        <a href="{{ url_for('index' )}}">Ir a inicio</a>
    {% endif %}

{% endblock %}


```

<h2>Include y Links</h2>
<p>El include es necesario para importar archivos a nuestra área de trabajo; sirven para reutilizar código que se va a repetir muchas veces, y así evitar que el desarrollo sea molestamente tedioso.
<p>Funcionan de la siguiente manera:

```
base.html
<body>
    <header>
        {% include 'navbar.html' %}
    </header>
    {% block content %} {% endblock %}
</body>


navbar.html
<nav>
    <ul>
        <li> <a href="{{url_for('index')}}">Ir a inicio.</a></li>
        <li><a href="https://platzi.com" target="_blank">Platzi.</a></li>
    </ul>
</nav>
```