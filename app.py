from decouple import config

print(config('MYSQL_HOST'))
print(config('MYSQL_PORT'))
print(config('MYSQL_USER'))
print(config('MYSQL_PWD'))