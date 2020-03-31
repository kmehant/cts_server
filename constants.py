import os

print (os.environ['PASS'])
print (os.environ['DBPASS'])

mail_pass = os.environ['PASS']
db_pass = os.environ['DBPASS']

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
MYSQL_PASSWORD=db_pass
MYSQL_DB='tFkLeQmDdy'

config={'CACHE_TYPE': 'simple'}