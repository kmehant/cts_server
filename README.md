# cts Server

We have deployed our cts server at 
```
https://pasp-api.herokuapp.com/ | https://git.heroku.com/pasp-api.git
```
and our db server at 
```
https://remotemysql.com/

```

## About
Basic flask server to interact with the mysql database server and other functionalities.

## MileStones
### Server
- [x] /
- [x] /login
- [x] /delete 
- [x] /signup
- [x] /forgot
- [x] /input get
- [x] /input post
- [x] /details
- [x] /stats
- [x] /gstats
- [x] cache implementation
- [x] dump some data into db


## How to Setup
### PASP server
* Fork this repo 
* clone this repo locally using git
* Move to the root folder.
* do `pip3 install -r requirements.txt`
* Once all the required packages are installed, run `python3 Main.py` to run the server.
* Any missing python modules, you can isntall them and add them to the `requirements.txt` file
### MySQL server
* you need to have your local MySQL server running
* to test this you can simply use your MySQL command line client and make a simple query
* use the pasp schema `pasp_db.sql` and load that onto a database with name `pasp_db` using MySQL workbench in windows. For mac or linux use the command `mysql -u root -p pasp_db < pasp_db.sql`
* In the Main.py file you can find different app.config variables. Configure them according to your local Mysql Server. Anyways host remains the same.
