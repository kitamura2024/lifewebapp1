"""
苦手診断「仕事・作業編」の機能ファイルです。
question_a.htmlにrender_template関数を使って変数を送信し、
表示させています。
"""

from flask import Blueprint, render_template, request, session, redirect, url_for
import random

#Blueprintを定義
quiz_bp_a = Blueprint('quiz_a', __name__, template_folder='../templates')
#初期化ルート
@quiz_bp_a.route("/quiz_a/init", methods=["GET"])
def quiz_init():
    # セッションのクリアと初期化
    session.clear()
    session["current_index"] = 0
    session["scores"] = {
        "multitask": 0,
        "creativity": 0,
        "forgetAction": 0,
        "forgetItem": 0,
        "planning": 0,
        "time": 0,
        "anxiety": 0,
        "careless": 0
    }
    # クイズメインページにリダイレクト
    return redirect(url_for("quiz_a.quiz"))

#初期化
multitask = 0 #マルチタスクが苦手
creativity = 0 #新しいことに取り組む、問題解決方法を自ら見つける、発想力（料理を考える）、収納や整理整頓
forgetAction = 0 #やるべきことをよく忘れる、聞いたことを忘れる
forgetItem = 0 #物をよく忘れる
planning = 0 #プランニング（行動の計画を立てること、優先順位）、片付けをやり始める、締め切り苦手
time = 0 #時間の管理が苦手
anxiety =0 #不安になりやすい
careless =0 #集中力が続かない、単純作業が苦手

def add_point(x):
    return x + 1

def judge(multitask, creativity, forgetAction, forgetItem,
          planning, time, anxiety, careless):
    scores = {
        "careless": int(careless),
        "multitask": int(multitask),
        "planning": int(planning),
        "forgetAction": int(forgetAction),
        "forgetItem": int(forgetItem),
        "time": int(time),
        "creativity": int(creativity),
        "anxiety": int(anxiety)
    }

    max_score = -1
    highest_scores = []

    for key, value in scores.items():
        if value > max_score:
            max_score = value
            highest_scores = [key]
        elif value == max_score and max_score > 0:
            highest_scores.append(key)

    if not highest_scores:
        return {"comment": """苦手な傾向は今回の結果からは見当たりませんでした。
                よろしければもう一つの診断も試してみてください。"""
                ,"url": "/question_btop","blog_title": "「苦手診断：コミュニケーション編」に進む >"}

    chosen_item = random.choice(highest_scores)

    if chosen_item == "careless":
        return {"comment": """あなたは単純作業や同じことの繰り返しの作業が苦手な傾向があるようです。
                集中力が続きにくいことや注意が他のことに向いてしまうことも多いかもしれません。
                下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
                ,"url":"/slow-at-routine-task", "blog_title": "「単純作業を素早くこなす」を読む >"}
    elif chosen_item == "multitask":
        return {"comment": """あなたは複数のことを同時に進めていくことが苦手な傾向があります。
                例えば、２つ以上の料理を同時進行で作ることや話を聞きながら作業を進めること等は
                やりにくさを感じることも多いのではないでしょうか。
                下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
                ,"url":"/forget-todo","blog_title": "「やるべきことを忘れる」を読む >"}
    elif chosen_item == "planning":
        return {"comment": """あなたは物事の見通しを立てることやスケジュールを作成することが苦手な傾向があるようです。
                計画的に進めることができないことで、締め切りに間に合わないことや優先順位をつけて
                行動できないことがあるかもしれません。
                下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
                ,"url": "/forget-todo","blog_title": "「やるべきことを忘れる」を読む >"}
    elif chosen_item == "forgetAction":
        return {"comment": """やるべきことを忘れることが多い傾向があると思われます。
                また複数の指示等、人から言われたことを忘れてしまうこともあるかもしれません。
                下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
                ,"url": "/forget-todo","blog_title": "「やるべきことを忘れる」を読む >"}
    elif chosen_item == "forgetItem":
        return {"comment": """物を忘れることが多い傾向があるようです。
                物を置いた場所が分からなくなることや無意識にどこかに置き忘れてしまうといったことがあるのではないでしょうか。
                以下の苦手対策を確認してみましょう。"""
                ,"url": "/often-forget-items","blog_title": "「置き忘れ」を読む >"}
    elif chosen_item == "time":
        return {"comment": """時間の管理が苦手な傾向があるようです。待ち合わせ時間に遅れることや締め切りに間に合わないこと等があるのではないでしょうか。
                時間の管理の苦手さは時間感覚の統合性の問題や先のことを見通すことの苦手が影響しているかもしれません。
                普段の生活の中で遅刻が多いと感じている方は、以下の苦手対策ページ一覧から【遅刻】を選択して対策を確認してみましょう。"""
                ,"url": "/always-late","blog_title": "「遅刻」を読む >"}
    elif chosen_item == "creativity":
        return {"comment": """新しい発想や解決策を求められると負担になることがあるかもしれません。
                下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
                ,"url": "/awkward-in-conversations","blog_title": "「雑談」を読む >"}
    elif chosen_item == "anxiety":
        return {"comment": """仕事や作業において苦手なことは少ないと思われます。何事も上手に進めていく力を持っておられるのでは
                ないでしょうか。ただし、人より不安になりやすい部分が
                あるかもしれません。上手くいかないときには自身の不安や緊張が影響していることもあるでしょう。
                不安や緊張が続くようであれば、誰かに話すことやしっかりとした休息をとることを検討してください。
                下の苦手対策もぜひ読んでみてくださいね。"""
                ,"url": "/anxiety","blog_title": "「不安と緊張」を読む >"}

    return {"comment": "予期せぬエラーが発生しました。", "url": "/", "blog_title": "トップページに戻る >"}

questions = [
    {"question": "『やるべきことや予定を忘れることがよくある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_a"},
    {"question": "『同じことの繰り返しや単純な作業が長時間続くと、強いストレスや疲労感を感じることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『予定していた時間に遅れることはほとんどない』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_c"},
    {"question": "『考えるより先に行動する方だ』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_d"},
    {"question": "『傘やスマートフォン等、ものをどこかに置き忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_e"},
    {"question": "『複数の作業を同時に進めることを好む（または、よくそうする）』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_f"},
    {"question": "『完了した作業に間違いがないか何度も確認をする』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_g"},
    {"question": "『何か行動するとき、自分で時間を決めて時間通りに行動することができる』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_h"},
    {"question": "『割とテキパキ動くことができる』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_i"},
    {"question": "『新しいことにワクワクしながら挑戦することが多い』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_j"},
]

#メインルート
@quiz_bp_a.route("/quiz_a", methods=["GET", "POST"])
def quiz():
    if "current_index" not in session or session.get("current_index") is None:
        session["current_index"] = 0
        session["scores"] = {
            "multitask": 0,
            "creativity": 0,
            "forgetAction": 0,
            "forgetItem": 0,
            "planning": 0,
            "time": 0,
            "anxiety": 0,
            "careless": 0
        }

    current_index = session["current_index"]
    scores = session["scores"]

    if request.method == "POST":
        answer = int(request.form.get("answer"))
        q = questions[current_index]

        if q["type"] == "personality_a" and answer in [1, 2]:
            scores["forgetAction"] += 2
        elif q["type"] == "personality_b" and answer in [1, 2]:
            scores["careless"] += 1
        elif q["type"] == "personality_c" and answer in [3, 4]:
            scores["planning"] += 1
            scores["time"] += 2
        elif q["type"] == "personality_d" and answer in [1, 2]:
            scores["creativity"] += 1
            scores["forgetItem"] += 1
        elif q["type"] == "personality_e" and answer in [1, 2]:
            scores["forgetItem"] += 2
            scores["forgetAction"] += 1
        elif q["type"] == "personality_f" and answer in [3, 4]:
            scores["multitask"] += 2
        elif q["type"] == "personality_g" and answer in [1, 2]:
            scores["anxiety"] += 2
            scores["careless"] += 1
        elif q["type"] == "personality_h" and answer in [3, 4]:
            scores["planning"] += 2
            scores["time"] += 1
        elif q["type"] == "personality_i" and answer in [3, 4]:
            scores["multitask"] += 1
            scores["careless"] += 1
        elif q["type"] == "personality_j" and answer in [3, 4]:
            scores["creativity"] += 2
            scores["anxiety"] += 1

        session["scores"] = scores
        session["current_index"] += 1
        
        #現在の質問番号を取得
        if session["current_index"] >= len(questions):
            result = judge(**scores)
            session.clear()
            #comment、urlの変数を結果を表示するurlに送る
            return render_template("quiz_a/result_a.html", comment=result["comment"], url=result["url"], 
                                   blog_title=result["blog_title"])

        return redirect(url_for("quiz_a.quiz"))

    # GET処理
    current_index = session["current_index"]
    question = questions[current_index]
    total_questions = len(questions)

    return render_template("quiz_a/question_a.html", question=question, current_index=current_index, total_questions=total_questions)