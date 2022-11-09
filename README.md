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
