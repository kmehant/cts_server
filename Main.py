from flask import request, jsonify, Response
import json
from flask_mail import Message

from utils import otp, present_date, executeSQL, rvalidate, svalidate, tvalidate
from initializer import cts, mail, cache




@cts.route('/')
def check():
    data = executeSQL('show tables',False,)
    return Response(response=json.dumps(data),status=200)


@cts.route('/login/t')
def tlogin():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     try: 
        pos = email.index('@') 
     except ValueError as e: 
        return Response(response='Invalid', status=401)
        pass
     domain = email[pos:]
     print(domain)
     if domain != "@nitandhra.ac.in":
        return Response(response='Failed', status=401)
     sd = executeSQL('select tid from teachers where temail="%s"', True, email)
     if sd is None:
        executeSQL('insert into teachers (temail) values("%s")', True, email)
     if onepass is not None:
         p = executeSQL('select tid from teachers where temail="%s" and tpin="%s"', True, email, onepass)
         if p is not None:
             return Response(response='Success', status=200)
         return Response(response='Failed', status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: "%s" \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         executeSQL('update teachers set tpin="%s" where temail="%s"', True, key, email)
         return Response(response='Success', status=200)


@cts.route('/login/s')
def slogin():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     try: 
        pos = email.index('@') 
     except ValueError as e: 
        return Response(response='Invalid', status=401)
        pass
     domain = email[pos:]
     if domain != "@student.nitandhra.ac.in":
        return Response(response='Failed', status=401)
     sd = executeSQL('select sid from students where Semail="%s"', True, email)
     print(sd)
     if sd is None:
        executeSQL('insert into students (Semail) values("%s")', True, email)
     if onepass is not None:
         p = executeSQL('select sid from students where Semail="%s" and spin="%s"', True, email, onepass)
         if p is not None:
             return Response(response='Success', status=200)
         return Response(response='Failed', status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: "%s" \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         executeSQL('update students set spin="%s" where Semail="%s"', True, key, email)
         return Response(response='Success', status=200)
     

@cts.route('/signup')
def signup():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     try: 
        pos = email.index('@') 
     except ValueError as e: 
        return Response(response='Invalid', status=401)
        pass
     domain = email[pos:]
     if domain != "@student.nitandhra.ac.in" or domain != "@nitandhra.ac.in":
        return Response(response='Failed', status=401)
     if domain == "@student.nitandhra.ac.in":
        i = executeSQL('select sid from students where Semail="%s"', True, email)
     else:
        i = executeSQL('select tid from teachers where temail="%s"', True, email)
     if domain == "@student.nitandhra.ac.in" and i is not None:
         executeSQL('insert into students (Semail) values("%s")', True, email)
     elif domain == "@nitandhra.ac.in" and i is not None:
         executeSQL('insert into teachers (temail) values("%s")', True, email)
     if onepass != "":
         if domain == "@student.nitandhra.ac.in":
             p = executeSQL('select spin from students where Semail="%s"', True, email)
         else:
             p = executeSQL('select tpin from teachers where temail="%s"', True, email)
         if p[0] == onepass:
             return Response(response='Success', status=200)
         return Response(response='Failed', status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: "%s" \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         if domain == "@student.nitandhra.ac.in":
             executeSQL('update students set spin="%s" where Semail="%s"', True, key, email)
         else:
             executeSQL('update teachers set tpin="%s" where temail="%s"', True, key, email)
         return Response(response='Success', status=200)


@cts.route('/login/r')
def rlogin():
     email = request.args.get('email')
     onepass = request.args.get('pin')
     if onepass is not None:
         p = executeSQL('select rid from resolvers where remail="%s" and rpin="%s"', True, email, onepass)
         if p is not None:
             return Response(response='Success', status=200)
         return Response(response='Failed', status=401)
     else:
         key = otp()
         with cts.app_context():
             msg = Message(subject="Single use resolver's pin for NIT Andhra Pradesh CTS login",
             sender=cts.config.get("MAIL_USERNAME"),
             recipients=[email],
             body='Single use pin: "%s" \n \n \n This is an auto generated mail. \n Please do not reply to this message or on this email address. \n For any query, please contact at 411843@student.nitandhra.ac.in \n Do not disclose any confidential information to anyone.' % key)
         mail.send(msg)
         executeSQL('update resolvers set rpin="%s" where remail="%s"', True, key, email)
         return Response(response='Success', status=200)


@cts.route('/tfiles/<token>')
def tfiles(token):
     vdata = tvalidate(token)
     data = request.headers['data']
     tags = request.headers['tags']
     if vdata is not None:
         cid = executeSQL('select cid from complaints where cdata="%s" and tags="%s"', True, data, tags)
         if cid is None:
            executeSQL('insert into complaints(cdata,tags) values ("%s","%s")', True, data, tags)
            cid = executeSQL('select cid from complaints where cdata="%s" and tags="%s"', True, data, tags)
            time_now = present_date()
            executeSQL('insert into tfiles(tid,cid,ftime) values (%d,%d, "%s")', True, vdata[0], cid, time_now)
         return Response(response='Success', status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/sfiles/<token>')
def sfiles(token):
     vdata = svalidate(token)
     data = request.headers['data']
     tags = request.headers['tags']
     if vdata is not None:
         cid = executeSQL('select cid from complaints where cdata="%s" and tags="%s"', True, data, tags)
         if cid is None:
            executeSQL('insert into complaints(cdata,tags) values ("%s","%s")', True, data, tags)
            cid = executeSQL('select cid from complaints where cdata="%s" and tags="%s"', True, data, tags)
            time_now = present_date()
            executeSQL('insert into sfiles(sid,cid,ftime) values (%d,%d, "%s")', True, vdata[0], cid, time_now)
         return Response(response='Success', status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/myscomplaints/<token>')
@cache.cached(timeout=100)
def myscomplaints(token):
     vdata = svalidate(token)
     if vdata is not None:
         data = executeSQL('select * from students,complaints, sfiles where students.sid=sfiles.sid and sfiles.cid=complaints.cid and students.sid = %d', False, vdata[0])
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/mytcomplaints/<token>')
@cache.cached(timeout=100)
def mytcomplaints(token):
     vdata = tvalidate(token)
     if vdata is not None:
         data = executeSQL('select * from teachers,complaints, tfiles where teachers.tid=tfiles.tid and tfiles.cid=complaints.cid and teachers.tid = %d', False, vdata[0])
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/mytcomplaints/r/<token>')
@cache.cached(timeout=100)
def mytcomplaintsr(token):
     vdata = tvalidate(token)
     if vdata is not None:
         data = executeSQL('select * from teachers,complaints, tfiles, resolves, resolvers where teachers.tid=tfiles.tid and tfiles.cid=complaints.cid and resolves.cid = complaints.cid and resolves.rid = resolvers.rid and teachers.tid = %d', False, vdata[0])
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/myscomplaints/r/<token>')
@cache.cached(timeout=100)
def myscomplaintsr(token):
     vdata = svalidate(token)
     if vdata is not None:
         data = executeSQL('select * from students,complaints, sfiles, resolves, resolvers where students.sid=sfiles.sid and sfiles.cid=complaints.cid and resolves.cid = complaints.cid and resolves.rid = resolvers.rid and students.sid = %d', False, vdata[0])
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/scomplaints/<token>')
@cache.cached(timeout=100)
def scomplaints(token):
     vdata = rvalidate(token)
     if vdata is not None:
         data = executeSQL('select * from students,complaints, sfiles where students.sid=sfiles.sid and sfiles.cid=complaints.cid ', False)
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/tcomplaints/<token>')
@cache.cached(timeout=100)
def tcomplaints(token):
     vdata = rvalidate(token)
     if vdata is not None:
         data = executeSQL('select * from teachers,complaints, tfiles where teachers.tid=tfiles.tid and tfiles.cid=complaints.cid ', False)
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


@cts.route('/complaints/u/<cid>/<token>')
def complaints(cid, token):
     vdata = rvalidate(token)
     exp = request.headers['exp']
     is_resolved = request.headers['is_resolved'] # 0/1
     is_valid = request.headers['is_valid'] # 0/1
     if vdata is not None:
         data = executeSQL('insert into resolves values(%d, %d, %d, %d,"%s")', False, vdata[0], cid,is_valid, is_resolved, exp)
         return Response(response=data, status=200)
     else:
         return Response(response='Failed', status=401)


if __name__ == '__main__':
    cts.run(threaded=True)