# Despliege de una app en Heroku

## Instalacion de heroku clic

Antes de empezar necesitaremos de la herramienta CURL, para instalarla, debemos de ejecutar en una terminal el siguiente comando.

```sh

$ sudo apt install curl

```

Para la instalacion en ubuntu o cualquier distro basada en debian que use el gesto de paquete apt-get, escribimos el siguiente comando:

```sh

$ curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

```
## Subida de proyecto al repositorio de heroku

Una vez instalado creamos una carpeta para el proyecto, y si ya tenemos una no situamos dentro de la misma con el comando:

```sh

$ cd nombre_carpeta_proyecto

```
Iniciamos un nuebo repositorio de git:
```sh
$ git init
```
Lo vinculamos al repositorio previamente creado en Heroku con el nombre de "headline-clase":
```sh
$ heroku git:remote -a headline-clase
```
Nos mostrara un mensaje para hacer login con nuetra cuenta heroku y luego de logearnos nos mostrara un mensaje como el siguiente:
```
Opening browser to https://cli-auth.heroku.com/auth/browser/74a11200-3fa4-4471-97d6...
Logging in... done
Logged in as santiago.amo.quintero@gmail.com
```
## *Importante* 

Debemos de crear un fichero de llamado **"requirements.txt"** y otro **profile**.

Una vez que el programa este en la carpeta y listo para ser desplegado en heroku introcimos los siguientes comandos:

```sh
# Añadimos el contenido de la carpeta a la zona de preparado para hace commit de git
$ git add .
# Hacemos un commit del estado actual del proyecto
$ git commit -am "Desplegando el proyecto headline de flask"
# Hacemos un push en la rama **master** del repositorio de Heroku con las herramienta git
$ git push heroku master
```
Luego del git push comenzara a instalar la dependencias especifocadas en el fichero "requirements.txt".

Una vea acabado nos dirigimos a la web con la url que nos otorga heroku.

[MI APP EN HEROKU](https://headline-clase.herokuapp.com/)

## Bicliografia Web

[DOC HEROKU CLI](https://devcenter.heroku.com/articles/heroku-cli)
[TUTORIAL APP TO HEROKU](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)