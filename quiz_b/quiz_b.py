"""
苦手診断「コミュニケーション編」の機能ファイルです。
question_b.htmlにrender_template関数を使って変数を送信し、
表示させています。
"""

from flask import Blueprint, render_template, request, session, redirect, url_for
import random

#Blueprintを定義
quiz_bp = Blueprint('quiz_b', __name__, template_folder='../templates')
#初期化ルート
@quiz_bp.route("/quiz_b/init", methods=["GET"])
def quiz_init_b():
    # セッションのクリアと初期化
    session.clear()
    session["current_index"] = 0
    session["scores"] = {
        "socialAnxiety" : 0, #対人不安
        "lackOfEmpathy" : 0, #抽象的なことに対する苦手
        "inattention" : 0, #衝動性
        "cognition" : 0 #不注意
    }
    # クイズメインページにリダイレクト
    return redirect(url_for("quiz_b.quiz_b"))
#初期化
socialAnxiety = 0 #対人不安
lackOfEmpathy = 0 #抽象的なことに対する苦手
inattention =0 #衝動性
cognition =0 #不注意

def add_point(x):
    return x + 1

def judge(socialAnxiety, lackOfEmpathy, inattention, cognition):
    scores = {
        "inattention": int(inattention),
        "lackOfEmpathy": int(lackOfEmpathy),
        "socialAnxiety": int(socialAnxiety),
        "cognition": int(cognition)
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
                ,"url": "/question_atop","blog_title": "「苦手診断：コミュニケーション編」に進む >"}

    chosen_item = random.choice(highest_scores)

    if chosen_item == "inattention":
        return {"comment":"""あなたは気持ちのままについ動いてしまうことや衝動的に動いてしまう傾向があるようです。
                思ったことを行動に移しやすいことは意見を多く述べることができたり、仕事をテキパキとこなすことができたりと、
                普段から多くの人の助けになっているはずです。一方で集中力が続きにくいことや注意が他のことに向いてしまうことも多いかもしれません。
                下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
                ,"url":"/often-forget-items", "blog_title": "「置き忘れ」を読む >"}
    elif chosen_item == "lackOfEmpathy":
        return {"comment":"""あなたは抽象的な内容を理解することや幅広いことに興味を持つことに苦手な傾向があるようです。
                雑談や会話の中で、相手の曖昧な表現が分かりにくいと感じたり、冗談が冗談だと分からないことがあるかもしれません。
                仕事等での決まった内容の言葉のやり取りであれば得意でも、雑談のように話す内容が決まっていない言葉のやり取りは苦手に感じたり、
                避けたくなったりすることがあるのではないでしょうか。
                下の苦手対策を確認してみましょう。"""
                ,"url":"/awkward-in-conversations", "blog_title": "「雑談」を読む >"}
    elif chosen_item == "socialAnxiety":
        return {"comment":"""あなたは社会的な不安が高い傾向があるようです。
                人の多い場所では不安が高くなったり、複数人と話すときに緊張したりすることがあるかもしれません。
                下の苦手対策の中から気になるものがあれば確認してみましょう。"""
                ,"url":"/anxiety", "blog_title": "「不安と緊張」を読む >"}
    elif chosen_item == "cognition":
        return {"comment":"""あなたは、やるべきことを忘れてしまうことが多い傾向があるようですね。
                特に、たくさんのタスクを抱えている時、どのように進めていけば良いか分からなくなって、混乱してしまうことがあるかもしれません。
                また、複数の指示を受けたり、人から言われたことを覚えていられなかったりすることもあるのではないでしょうか。
                やるべきことが多いと、どうしてもストレスを感じてしまいますが、いくつか対策できることがあるかもしれません。
                もし、下の苦手対策の中に気になるものがあれば、ぜひ確認してみてください。
                """
                ,"url":"/forget-todo", "blog_title": "「やるべきことを忘れる」を読む >"}

    return {"comment": "予期せぬエラーが発生しました。", "url": "/", "blog_title": "トップページに戻る >"}

questions = [
    {"question": "『必要なことがあっても、人に声をかけるのをためらうことがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_a"},
    {"question": "『飲み会や大人数での食事会は避けている。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『対面で話すよりも電話で話す方が楽だ。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_c"},
    {"question": "『雑談や世間話をするのが好きだ』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_d"},
    {"question": "『相手の話を聞いていられないときがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_e"},
    {"question": "『冗談がわからないときがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_f"},
    {"question": "『何かをするときには、一人でするよりも他の人と一緒にする方が好きだ。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_g"},
    {"question": "『話し方が失礼だと言われることがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_h"},
    {"question": "『初対面の人と会うことはできるだけ避けたい。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_i"},
    {"question": "『人から悪く言われているのではと感じることがよくある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_j"},
]
questions_with_index = list(enumerate(questions))  #質問リストを作成

@quiz_bp.route("/quiz_b", methods=["GET", "POST"])
def quiz_b():
    if "current_index" not in session or session.get("current_index") is None:
        session["current_index"] = 0
        session["scores"] = {
            "socialAnxiety": 0,
            "lackOfEmpathy": 0,
            "inattention": 0,
            "cognition": 0
        }

    current_index = session["current_index"]
    scores = session["scores"]

    if request.method == "POST":
        answer = int(request.form.get("answer"))
        q = questions[current_index]

        if q["type"] == "personality_a" and answer in [1, 2]:
            scores["socialAnxiety"] += 1
            scores["cognition"] += 1
        elif q["type"] == "personality_a" and answer in [4]:
            scores["inattention"] += 1
        elif q["type"] == "personality_b" and answer in [1, 2]:
            scores["socialAnxiety"] += 1
        elif q["type"] == "personality_c" and answer in [3, 4]:
            scores["inattention"] += 1
        elif q["type"] == "personality_d" and answer in [3, 4]:
            scores["lackOfEmpathy"] += 1
            scores["cognition"] += 1
        elif q["type"] == "personality_e" and answer in [1, 2]:
            scores["lackOfEmpathy"] += 1
            scores["inattention"] += 1
        elif q["type"] == "personality_f" and answer in [1, 2]:
            scores["lackOfEmpathy"] += 2
        elif q["type"] == "personality_g" and answer in [3, 4]:
            scores["socialAnxiety"] += 1
        elif q["type"] == "personality_h" and answer in [1, 2]:
            scores["inattention"] += 1
        elif q["type"] == "personality_i" and answer in [1, 2]:
            scores["socialAnxiety"] += 1
            scores["cognition"] += 1
        elif q["type"] == "personality_j" and answer in [1, 2]:
            scores["cognition"] += 1

        session["scores"] = scores
        session["current_index"] += 1

        if session["current_index"] >= len(questions):
            result = judge(**scores)
            session.clear()
            return render_template("quiz_b/result_b.html", comment=result["comment"], url=result["url"], blog_title=result["blog_title"])
        
        #redirectだと次の質問への移行に時間がかかるため、使用していません。
        current_index = session["current_index"]
        question = questions[current_index]
        total_questions = len(questions)

        return render_template("quiz_b/question_b.html", question=question, current_index=current_index, total_questions=total_questions)

        

    # GET処理
    current_index = session["current_index"]
    question = questions[current_index]
    total_questions = len(questions)

    return render_template("quiz_b/question_b.html", question=question, current_index=current_index, total_questions=total_questions)