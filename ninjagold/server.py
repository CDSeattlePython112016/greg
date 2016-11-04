from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "SEGw454r3t4"

@app.route('/')
def index():
    if 'activity_log' not in session:
        session['activity_log']=[]
    if 'your_gold' not in session:
        session['your_gold']=0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == "farm":
        new_gold=random.randint(10,20)
        session['your_gold']+=new_gold
    elif building == "cave":
        new_gold=random.randint(5,10)
        session['your_gold']+=new_gold
    elif building == "house":
        new_gold=random.randint(2,5)
        session['your_gold']+=new_gold
    elif building == "casino":
        new_gold=random.randint(-50,50)
        session['your_gold']+=new_gold

    print(new_gold)
    new_activity = {"actText": "You {} {} from the {}".format("earned" if new_gold > 0 else "lost", abs(new_gold), building), "actColor": "green" if new_gold > 0 else "red"}
    session['activity_log'].append(new_activity)

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
