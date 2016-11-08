from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = '32r2wf4r32'
mysql = MySQLConnector(app,'friendsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    friends = mysql.query_db('SELECT * FROM friends')
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query="INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {'first_name': request.form['fname'],
             'last_name':  request.form['lname'],
             'occupation': request.form['occupation']}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    print('Made it to update')
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['fname'],
             'last_name':  request.form['lname'],
             'occupation': request.form['occupation'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query="SELECT * FROM friends WHERE id = :specific_id"
    data={'specific_id': id}
    friends = mysql.query_db(query,data)
    return render_template('edit_user.html', one_friend=friends[0])

@app.route('/friends/<id>/delete')
def delete(id):
    # DELETE FROM table_name WHERE condition(s)
    query='DELETE FROM friends WHERE id= :id'
    data={'id': id}
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)
