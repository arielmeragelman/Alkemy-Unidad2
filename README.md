# Alkemy-Unidad2
Archivos de Configuración - Práctico


Utilizando los conceptos aprendidos en el módulo1
- Archivos de Configuración, resolver el siguiente ejercicio:


1- Instalar VSC

2- Crear un proyecto Python

3- Crear un nuevo ambiente virtual llamado venv-decouple

4- Instalar Decouple

5- Generar un archivo con variables de entorno para acceder a

una base de datos MySQL.

6- Generar una aplicación Python para mostrar por pantalla las

variables de entorno, utilizando Decouple y Placeholders

7- Instalar Dotenv

8- Modificar la aplicación Pyton desarrollada en el punto 6 para
mostrar las variables de entorno por pantalla utilizado dotenv



---------------------------

Ejemplo de pasos a seguir para simular el ejercicio

(base) arielmeragelman@debian:~/Entornos$ mkdir Unidad2
(base) arielmeragelman@debian:~/Entornos$ cd Unidad2
(base) arielmeragelman@debian:~/Entornos/Unidad2$ python -m venv venv-decouple
(base) arielmeragelman@debian:~/Entornos/Unidad2$ source venv-decouple/bin/activate
(venv-decouple) (base) arielmeragelman@debian:~/Entornos/Unidad2$ python -m pip install decouple
Collecting decouple
  Downloading decouple-0.0.7.tar.gz (3.3 kB)
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for decouple, since package 'wheel' is not installed.
Installing collected packages: decouple
  Running setup.py install for decouple ... done
Successfully installed decouple-0.0.7


IMPORTANTE!

La libreria decouple no funciona correctamente en algunos casos por lo que se recomienda usar python-decouple

python -m pip install python-decouple
Collecting python-decouple
  Using cached python_decouple-3.6-py3-none-any.whl (9.9 kB)
Installing collected packages: python-decouple
Successfully installed python-decouple-3.6


Lo ejecutamos 

(venv-decouple) (base) arielmeragelman@debian:~/Entornos/Unidad2$ python app.py
localhost
3030
usuarioadministrador
passwordsecreta




-----------------------

Se debe crear un archivo .env en el directorio donde esta nuestro app.py, el mismo por razones de seguridad no debe quedar en el historial de github pero se deja como debe conformarse usando datos no reales

MYSQL_HOST=localhost
MYSQL_PORT=3030
MYSQL_USER=usuarioadministrador
MYSQL_PWD=passwordsecreta

-----------------

Importante!!!
Para la segunda parte del ejercicio se debe considerar que el paquete dotenv puede generar conflictos por lo que instalamos python-dotenv

venv-decouple) (base) arielmeragelman@debian:~/Entornos/Unidad2/Alkemy-Unidad2$ python -m pip install python-dotenv
Collecting python-dotenv
  Using cached python_dotenv-0.21.0-py3-none-any.whl (18 kB)
Installing collected packages: python-dotenv
Successfully installed python-dotenv-0.21.0
WARNING: You are using pip version 22.0.4; however, version 22.3.1 is available.
You should consider upgrading via the '/home/arielmeragelman/Entornos/Unidad2/venv-decouple/bin/python -m pip install --upgrade pip' command.
