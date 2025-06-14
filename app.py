from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    total_bill = float(request.form['bill'])
    tip_percent = float(request.form['tip'])
    people = int(request.form['people'])

    tip_amount = (tip_percent / 100) * total_bill
    total_amount = total_bill + tip_amount
    per_person = total_amount / people

    return render_template('result.html', total=total_amount, each=per_person)

if __name__ == '__main__':
    app.run(debug=True)
