from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('doutaku.html')

@app.route('/model1')
def model1():
    return render_template('doutaku1.html')

@app.route('/model2')
def model2():
    return render_template('doutaku2.html')

if __name__ == '__main__':
    app.run(debug=True)