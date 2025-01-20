from flask import Blueprint, render_template, request

#Blueprintを定義
quiz_bp_a = Blueprint('quiz_a', __name__, template_folder='../templates')

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
    if int(careless) >= 2:
        return """あなたは単純作業や同じことの繰り返しの作業が苦手な傾向があるようです。
            集中力が続きにくいことや注意が他のことに向いてしまうことも多いかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(multitask) >= 2:
        return """あなたは複数のことを同時に進めていくことが苦手な面があるようです。
            例えば、２つ以上の料理を同時進行で作ることや話を聞きながら作業を進めること等は
            やりにくさを感じることも多いのではないでしょうか。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(planning) >= 2:
        return """あなたは物事の見通しを立てることやスケジュールを作成することが苦手な傾向があるようです。\
            計画的に進めることができないことで、締め切りに間に合わないことや優先順位をつけて
            行動できないことがあるかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(forgetAction) >= 1:
        return """やるべきことを忘れることが多い傾向があると思われます。
            また複数の指示等、人から言われたことを忘れてしまうこともあるかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(forgetItem) >= 1:
        return """物を忘れることが多い傾向があるようです。
            物を置いた場所が分からなくなることや無意識にどこかに置き忘れてしまうといったことがあるのではないでしょうか。
            以下の苦手対策ページ一覧から【置き忘れ】を選択して対策を確認してみましょう。"""
    elif int(time) >= 2:
        return """時間の管理が苦手な傾向があるようです。待ち合わせ時間に遅れることや締め切りに間に合わないこと等があるのではないでしょうか。\
            時間の管理の苦手さは時間感覚の統合性の問題や先のことを見通すことの苦手が影響しているかもしれません。
            普段の生活の中で遅刻が多いと感じている方は、以下の苦手対策ページ一覧から【遅刻】を選択して対策を確認してみましょう。"""
    elif int(creativity) >= 2:
        return """新しい発想や解決策を求められると負担になることがあるかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(anxiety) >= 1:
        return """様々なことに対して苦手はあまりないようです。ただし、人より不安になりやすい部分が
            あるかもしれません。上手くいかないときには自身の不安や緊張が影響していることもあるでしょう。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    else:
        return """苦手な傾向は今回の結果からは見当たりませんでした。
            他の診断をお試しいただくか、下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""

questions = [
    {"question": "『やるべきことや予定を忘れることがよくある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_a"},
    {"question": "『同じことの繰り返しや単純な作業が続くと、ひどく疲れを感じることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『予定していた時間に遅れることはほとんどない』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_c"},
    {"question": "『整理整頓や物をきれいに並べることが好き』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_d"},
    {"question": "『傘やスマートフォン等、ものをどこかに置き忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_e"},
    {"question": "『複数の作業はできる限り同時進行で進めていきたい』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_f"},
    {"question": "『完了した作業に間違いがないか何度も確認をする』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_g"},
    {"question": "『何か行動するとき、自分で時間を決めて時間通りに行動することができる』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_h"},
    {"question": "『割とテキパキ動くことができる』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_i"},
    {"question": "『パズルや謎解きゲームのようにじっくりと考えたり推理したりすることが好きだ』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_j"},
]
questions_with_index = list(enumerate(questions))  # インデックス付きリストを作成

@quiz_bp_a.route("/quiz_a", methods=["GET", "POST"])
def quiz():
    global multitask, creativity, forgetAction, forgetItem, planning, time, anxiety, careless
    if request.method == "POST":
        for i, question in enumerate(questions):
            answer = request.form.get(f"q{i+1}") #回答した値を取得
            if not answer:
                continue

            #ポイントの加算
            if question["type"] == "personality_a":
                if int(answer) == 0 or 1:
                    forgetAction == add_point(forgetAction)
            elif question["type"] == "personality_b":
                if int(answer) == 0 or 1:
                    careless = add_point(careless)
            elif question["type"] == "personality_c":
                if int(answer) == 2 or 3:
                    planning = add_point(planning)
                    time = add_point(time)
            elif question["type"] == "personality_d":
                if int(answer) == 2 or 3:
                    creativity = add_point(creativity)
            elif question["type"] == "personality_e":
                if int(answer) == 0 or 1:
                    forgetItem = add_point(forgetItem)
            elif question["type"] == "personality_f":
                if int(answer) == 2 or 3:
                    multitask = add_point(multitask)
            elif question["type"] == "personality_g":
                if int(answer) == 0 or 1:
                    anxiety = add_point(anxiety)
            elif question["type"] == "personality_h":
                if int(answer) == 2 or 3:
                    planning = add_point(planning)
                    time = add_point(time)
            elif question["type"] == "personality_i":
                if int(answer) == 2 or 3:
                    multitask = add_point(multitask)
                    careless = add_point(careless)
            elif question["type"] == "personality_j":
                if int(answer) == 2 or 3:
                    creativity = add_point(creativity)

        result = judge(multitask, creativity, forgetAction, forgetItem,
               planning, time, anxiety, careless)
        return render_template("quiz_a/question_a.html", result=result, questions=questions, questions_with_index=questions_with_index, multitask=multitask, creativity=creativity, forgetAction=forgetAction, forgetItem=forgetItem,
          planning=planning, time=time, anxiety=anxiety, careless=careless)
    
    #初期化またはGETリクエストのとき
    multitask = 0
    creativity = 0
    forgetAction = 0
    forgetItem = 0
    planning = 0
    time = 0 
    anxiety =0 
    careless =0
    return render_template("quiz_a/question_a.html", questions=questions, questions_with_index=questions_with_index, multitask=multitask, creativity=creativity, forgetAction=forgetAction, forgetItem=forgetItem,
          planning=planning, time=time, anxiety=anxiety, careless=careless, result=None)
