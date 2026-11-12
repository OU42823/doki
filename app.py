from flask import Flask, render_template

app = Flask(__name__)

# 最初の選択画面（トップページ）
@app.route('/')
def index():
    return render_template('doutaku.html')

# 1つ目のモデル（doutaku.usdz）を表示するページ
@app.route('/model1')
def model1():
    return render_template('doutaku1.html')

# 2つ目のモデル（doutaku2.usdz）を表示するページ
@app.route('/model2')
def model2():
    return render_template('doutaku2.html')

if __name__ == '__main__':
    app.run(debug=True)