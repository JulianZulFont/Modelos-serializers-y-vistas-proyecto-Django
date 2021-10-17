# Modelos-serializers-y-vistas-proyecto-Django
Archivos de los modelos, serializers y vistas para entidades, usuario, cuenta  y factura , parte de un CRUD hecho con Django y Django rest framework


Se parte de la base que se tiene ya un proyecto base creado y con las configuraciones elementales e inciales 

Esto hace parte de lo concerniente específicamente a la creación de modelos, sus serializers correspondientes, vistas y URLs, para la manipulación de 
las tablas de nuestra base de datos, aqui se tienen los serializers para modelos de usuario, cuenta de usuario (account), factura, entre otros.

Posteriormente a estos se les tiene que hacer su respectivo Serializer a cada modelo, es decir , como será su representación dependiendo de si nos llega un formato JSON
o una URL para hacer determinada petición al programa para hacer algún tipo de cambio dentro de la base de datos, por ejemplo, un formato de petición para crear elementos
o eliminarlos de la base de datos

Después se tienen las vistas, estas hacen función de controlador dentro del programa, determinarán la forma de crear, ver, actualizar o eliminar elementos o registros de la
base de datos

Y para finalizar, las URL para visualizar esto

Además a esto se tienen archivos hecho en bloc de notas con ejemplos con distintas operaciones para ingresar elementos a determinadas tablas, borrarlos, actualizarlos o crearlos
(pruebas que se pueden hacer en el navegador ejecutando el server (python manage.py runserver), o con los servicios de la página web de "Postman"

Este repositorio no contiene todos los archivos de un proyento en django y django rest framework completo, solo los archivos para implementar específicamente estos ejemplos 
básicos en los archivos de modelos, vistas y serializers dentro de un proyecto Django y quizás algún otro archivo mas como los settings en la carpete de proyecto general
