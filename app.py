from decouple import config


print("Los datos de la conexion son")
print(f"Host: {config('MYSQL_HOST')} PUERTO: {config('MYSQL_PORT')} USUARIO: {config('MYSQL_USER')} PASSWORD: {config('MYSQL_PWD')}   ")
