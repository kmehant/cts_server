from flask import request, jsonify, Response
import json
from flask_mail import Message

from utils import otp, present_date, executeSQL, validate, dumpDB, deleteDB, \
    numberOf, maximumCount, minimumCount, numberOfEach, getFactor
from initializer import cts, mail, cache




@cts.route('/')
@cache.cached(timeout=60)
def check():
    data = executeSQL('show tables',False,)
    return Response(response=json.dumps(data),status=200)


@cts.route('/login')
def login():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     try: 
        pos = email.index('@') 
     except ValueError as e: 
        return Response(response=jsonify('Invalid'), status=401)
        pass
     domain = email[pos:]
     if (domain != "student.nitandhra.ac.in" or domain != "nitandhra.ac.in")
        return Response(response=jsonify('Failed'), status=401)
     if onepass != "":
         if (domain == "student.nitandhra.ac.in")
             p = executeSQL('select sid from students where Semail=%s and spin=%s', True, email, onepass)
         else:
             p = executeSQL('select tid from teachers where temail=%s and tpin=%s', True, email, onepass)
         if None not in p:
             return Response(response=jsonify('Success'), status=200)
         return Response(response=jsonify('Failed'), status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: %s \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         if (domain == "student.nitandhra.ac.in")
             executeSQL('update students set spin="%s" where Semail="%s"', True, key, email)
         else:
             executeSQL('update teachers set tpin="%s" where temail="%s"', True, key, email)
         return Response(response=jsonify('Success'), status=200)
     

@cts.route('/signup')
def signup():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     try: 
        pos = email.index('@') 
     except ValueError as e: 
        return Response(response=jsonify('Invalid'), status=401)
        pass
     domain = email[pos:]
     if domain != "student.nitandhra.ac.in" or domain != "nitandhra.ac.in":
        return Response(response=jsonify('Failed'), status=401)
     if domain == "student.nitandhra.ac.in":
        i = executeSQL('select sid from students where Semail=%s', True, email)
     else:
        i = executeSQL('select tid from teachers where temail=%s', True, email)
     if domain == "student.nitandhra.ac.in" and None not in i:
         executeSQL('insert into students (Semail) values(%s)', True, email)
     elif domain == "nitandhra.ac.in" and None not in i:
         executeSQL('insert into teachers (temail) values(%s)', True, email)
     if onepass != "":
         if domain == "student.nitandhra.ac.in":
             p = executeSQL('select spin from students where Semail=%s', True, email)
         else:
             p = executeSQL('select tpin from teachers where temail=%s', True, email)
         if p[0] == onepass:
             return Response(response=jsonify('Success'), status=200)
         return Response(response=jsonify('Failed'), status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: %s \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         if domain == "student.nitandhra.ac.in":
             executeSQL('update students set spin="%s" where Semail="%s"', True, key, email)
         else:
             executeSQL('update teachers set tpin="%s" where temail="%s"', True, key, email)
         return Response(response=jsonify('Success'), status=200)


@cts.route('/rlogin')
def login():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     if onepass != "":
         p = executeSQL('select rid from resolvers where remail=%s and rpin=%s', True, email, onepass)
         if None not in p:
             return Response(response=jsonify('Success'), status=200)
         return Response(response=jsonify('Failed'), status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use resolver's pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: %s \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         executeSQL('update resolvers set rpin="%s" where remail="%s"', True, key, email)
         return Response(response=jsonify('Success'), status=200)


if __name__ == '__main__':
    cts.run(threaded=True)