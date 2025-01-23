from flask import Flask
from flask import render_template,request
import joblib

app = Flask(__name__)

model = joblib.load("student.pkl")
@app.route("/", methods=['GET','POST'])

def index():
    if request.method == 'POST':
        hours = float(request.form['hours'])#hours ki value web page se lena 
        prediction=model.predict([[hours]])#pridiction karna 
        result='pass' if prediction[0] ==1 else 'fail'
        return render_template('index.html',result=result,hours=hours)
        
    return render_template('index.html')#get post phli bar khulne vala page 



app.run(debug=True)