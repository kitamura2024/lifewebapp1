from flask import Flask, render_template

app = Flask(__name__)

@app.route('/top')
@app.route('/')#【デコレーター】引数であるURLにアクセスされた場合に下の関数を実行する
def top():
    return render_template('top.html')

@app.route('/shindan')#ルーティング
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/nigate_a1/<int:id>')
def nigate_a1(id):
    return render_template('nigate_a1.html', show_id=id)

@app.route('/nigate_a2/')
def nigate_a2():
    return render_template('nigate_a2.html')

#run() メソッド
if __name__ == '__main__':
    app.run(debug=True)
