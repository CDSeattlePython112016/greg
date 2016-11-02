from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['languages']
    comments = request.form['comments']
    return render_template("result.html", resname=name, resloc=location, reslang=language, rescom=comments)

app.run(debug=True)
