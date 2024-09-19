from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    age = int(request.form['age'])
    cholesterol = float(request.form['cholesterol'])
    blood_pressure = float(request.form['blood_pressure'])
    glucose = float(request.form['glucose'])
    bmi = float(request.form['bmi'])

    
    recommendation = ""
    
    if cholesterol > 240 or blood_pressure > 140 or glucose > 100 or bmi > 30:
        recommendation = "higher chance of heart disease."
    else:
        recommendation = "you seems Healthy"

    return render_template('result.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)