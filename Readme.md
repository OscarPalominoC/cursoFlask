## <h1> Curso de Flask</h1>

<h2>Contenido</h2>

- <a href="#Introducción">Introducción</a>
- <a href="#cómo-funcionan-las-aplicaciones-web">¿Cómo funcionan las aplicaciones web?</a>
- <a href="#qué-es-flask">¿Qué es Flask?</a>
- <a href="#hello-world-flask">Hello World Flask</a>
- <a href="#debugging-en-flask">Debugging en Flask</a>
- <a href="#request-y-response">Request y Response</a>

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

