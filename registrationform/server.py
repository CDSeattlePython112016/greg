from flask import Flask, render_template, redirect, request, session, flash

import re, string
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^[A-Z0-9]')

app = Flask(__name__)
app.secret_key = "4hgteghjh23"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    error = 0
    email = request.form['email']
    if len(email) < 1:
        flash("Email cannot be blank!")
        error+=1
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        error+=1
    else:
        session['email']=email
    firstname = request.form['firstname']
    if len(firstname) < 1:
        flash("First name cannot be blank!")
        error+=1
    elif not firstname.isalpha():
        flash("First name can only contain letters.")
        error+=1
    else:
        session['firstname']=firstname
    lastname = request.form['lastname']
    if len(lastname) < 1:
        flash("Last name cannot be blank!")
        error+=1
    elif not lastname.isalpha():
        flash("Last name can only contain letters.")
        error+=1
    else:
        session['lastname']=lastname
    if len(request.form['birthdate']) < 1:
        flash("Birth Date is required.")
        return redirect('/')
    birthdate = datetime.strptime(request.form['birthdate'],"%Y-%m-%d")
    if birthdate >= datetime.today():
        flash("Birth Date must be earlier than today.")
        error+=1
    pass1 = request.form['password']
    pass2 = request.form['passwordcfm']
    if pass1 != pass2:
        flash("Passwords do NOT match!")
        error+=1
    if len(pass1) < 8:
        flash("Password must be at least 8 characters")
        error+=1
    elif not PASS_REGEX.match(pass1):
        flash("Password must contain at least 1 capital letter and 1 number.")
        error+=1
    if not error > 0:
        flash("Thanks for submitting your information.")
    return redirect('/')

app.run(debug=True)
