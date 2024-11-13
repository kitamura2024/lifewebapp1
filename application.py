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

#▼▼▼ここから【制御文】▼▼▼
#商品クラス
""" class Item:
    def __init__(self, id, name) :
        self.id = id
        self.name = name
    def __str__(self):
        return f'商品ID : {self.id} 商品名 : {self.name}'

#繰り返し
@app.route("/for_list")
def show_for_list():
    item_list = [Item(1, "団子"), Item(2, "肉まん"), Item(3, "どら焼き")]
    return render_template('for_list.html', items = item_list)
 """