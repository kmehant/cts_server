import os

print (os.environ['PASS'])

mail_pass = os.environ['PASS']
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "411843@student.nitandhra.ac.in",
    "MAIL_PASSWORD": mail_pass
}

# production hosting values are given below

MYSQL_HOST='remotemysql.com'
MYSQL_USER='tFkLeQmDdy'
MYSQL_PASSWORD='Ng3u9avM2J'
MYSQL_DB='tFkLeQmDdy'

config={'CACHE_TYPE': 'simple'}