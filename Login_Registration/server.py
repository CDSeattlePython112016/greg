from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key='erig843n34fg8rns'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_demo')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    query='SELECT * FROM users WHERE email=:email;'
    data={'email': request.form['email']}
    user=mysql.query_db(query, data)

    if not user:
        flash('Email or password invalid')
        return redirect('/')

    user=user[0]

    if bcrypt.check_password_hash(user['password'], request.form['password']):
        session['user_id'] = user['id']
        return redirect('/success')
    else:
        flash('Email or password invalid')
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    error=0
    query='SELECT * FROM users WHERE email=:email;'
    data={'email': request.form['email']}
    user=mysql.query_db(query, data)
    if not len(request.form['first_name']) > 1:
        error+=1
        flash('First name must be at least 2 characters')
    elif not NAME_REGEX.match(request.form['first_name']):
        error+=1
        flash('First name can only contain letters')

    if not len(request.form['last_name']) > 1:
        error+=1
        flash('Last name must be at least 2 characters')
    elif not NAME_REGEX.match(request.form['last_name']):
        error+=1
        flash('Last name can only contain letters')

    if not EMAIL_REGEX.match(request.form['email']):
        error+=1
        flash('Invalid email address')
    elif user:
        error+=1
        flash('Email already registered')

    if not request.form['password']:
        error+=1
        flash('Please enter a password')
    elif len(request.form['password']) < 8:
        error+=1
        flash('Password must be at least 8 characters')
    elif request.form['password'] != request.form['confirm']:
        error+=1
        flash('Passwords do not match')

    if error > 0:
        return redirect('/')
    else:
        query="INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data={
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'pw_hash': bcrypt.generate_password_hash(request.form['password'])
        }
        session['user_id'] = mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')

    query='SELECT * FROM users WHERE id=:id'
    data={'id': session['user_id']}
    user=mysql.query_db(query, data)
    return render_template('success.html', user=user[0])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
