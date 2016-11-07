from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "089jwe89mn34f"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja/')
def tmnt():
    group=True
    return render_template('ninja.html', group=group)

@app.route('/ninja/<color>')
def ninja(color):
    group=False
    return render_template('ninja.html', color=color, group=group)

app.run(debug=True)
