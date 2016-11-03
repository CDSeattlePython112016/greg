from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'iohhw8389e'

@app.route('/', methods=['GET'])
def index():
    getNumber()
    return render_template('index.html', number=session['number'])

def getNumber():
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    if session['guess'] == session['number']:
        session['result'] = 'win'
    elif session['guess'] > session['number']:
        session['result'] = 'high'
    elif session['guess'] < session['number']:
        session['result'] = 'low'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
