import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
Host = os.getenv('MYSQL_HOST')
Puerto = os.getenv('MYSQL_PORT')
Usuario = os.getenv('MYSQL_USER')
Password = os.getenv('MYSQL_PWD')

print("Los datos de la conexion son")
print(f"Host: {Host} PUERTO: {Puerto} USUARIO: {Usuario} PASSWORD: {Password}   ")