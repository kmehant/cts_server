
from flask import Flask
from flask_mysqldb import MySQL
from constants import mail_settings, MYSQL_HOST, MYSQL_PASSWORD, \
    MYSQL_USER, MYSQL_DB, config
from flask_mail import Mail, Message
from flask_caching import Cache


cts = Flask(__name__) # cts server


# Required configuration
cts.config['MYSQL_HOST'] = MYSQL_HOST
cts.config['MYSQL_USER'] = MYSQL_USER
cts.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
cts.config['MYSQL_DB'] = MYSQL_DB
cts.config.update(mail_settings)
cts.config["CACHE_TYPE"] = "simple"

mail = Mail(cts) # mail handler
mysql = MySQL(cts) # db handler
cache = Cache(cts, config) #cache handler