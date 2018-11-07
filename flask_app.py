# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
import json
import mysql.connector
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'anand'
app.config['MYSQL_DATABASE_PASSWORD'] = 'asura22nov'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_DB']= 'tbl_user'

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
'''_hashed_password = generate_password_hash(_password)

cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
data = cursor.fetchall()
	if len(data) is 0:
        conn.commit()
        	return json.dumps({'message':'User created successfully !'})
	else:
        	return json.dumps({'error':str(data[0])})
'''


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showsignup')
def showsignup():
    return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def signup():
        # read the posted values from the UI
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        #return json.dumps({'status':'OK','user':_name,'pass':_password});
        # validate the received values

        '''if _name and _email and _password:
                return json.dumps({'html':'<span>All fields good !!</span>'})
        else:
                return json.dumps({'html':'<span>Enter the required fields</span>'})
        #return render_template('signup.html')
'''
	_hashed_password = generate_password_hash(_password)

	cursor.callproc('sp_createUser',(_name,_email,_hashed_password))

	data = cursor.fetchall()
	print(data)
        if len(data) is 0:
        	conn.commit()
                return json.dumps({'message':'User created successfully !'})
        else:
                return json.dumps({'error':str(data[0])})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

