from flask import Blueprint, render_template, request

#Blueprintを定義
quiz_bp = Blueprint('quiz_b', __name__, template_folder='../templates')

#初期化
socialAnxiety = 0
lackOfEmpathy = 0
inattention =0 
cognition =0

def add_point(x):
    return x + 1

def judge(socialAnxiety, lackOfEmpathy, inattention, cognition):
    if int(inattention) >= 2:
        return """あなたは気持ちのままについ動いてしまうことや衝動的に動いてしまう傾向があるようです。
            集中力が続きにくいことや注意が他のことに向いてしまうことも多いかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(lackOfEmpathy) >= 2:
        return """あなたは抽象的な内容を理解することや幅広いことに興味を持つことに苦手な傾向があるようです。
            雑談や会話の中で、相手の曖昧な表現が分かりにくいと感じたり、冗談が冗談だと分からないことがあるかもしれません。\
            仕事等での決まった内容の言葉のやり取りであれば得意でも、雑談のように話す内容が決まっていない言葉のやり取りは苦手に感じたり、\
            避けたくなったりすることがあるのではないでしょうか。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(socialAnxiety) >= 2:
        return """あなたは社会的な不安が高い傾向があるようです。
            人の多い場所では不安が高くなったり、複数人と話すときに緊張したりすることがあるかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""
    elif int(cognition) >= 2:
        return """やるべきことを忘れることが多い傾向があると思われます。
            また複数の指示等、人から言われたことを忘れてしまうこともあるかもしれません。
            下の苦手対策一覧の中から気になるものがあれば確認してみましょう。"""

questions = [
    {"question": "『伝えなければならないことがあるとき、声をかけるのを躊躇してしまうことがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_a"},
    {"question": "『飲み会や大人数での食事会は避けている。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『対面で話すよりも電話で話す方が楽だ。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_c"},
    {"question": "『特に意味がないような雑談が好きだ。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_d"},
    {"question": "『相手の話を聞いていられないときがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_e"},
    {"question": "『冗談がわからないときがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_f"},
    {"question": "『何かをするときには、一人でするよりも他の人と一緒にする方が好きだ。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_g"},
    {"question": "『話し方が失礼だと言われることがある。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_h"},
    {"question": "『初対面の人と会うことはできるだけ避けたい。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_i"},
    {"question": "『よく裏で自分の悪口を言われているように思う。』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_j"},
]
questions_with_index = list(enumerate(questions))  # インデックス付きリストを作成

@quiz_bp.route("/quiz_b", methods=["GET", "POST"])
def quiz():
    global socialAnxiety, lackOfEmpathy, inattention, cognition
    if request.method == "POST":
        for i, question in enumerate(questions):
            answer = request.form.get(f"q{i+1}") #回答した値を取得
            if not answer:
                continue

            #ポイントの加算
            if question["type"] == "personality_a":
                if int(answer) == 0 or 1:
                    socialAnxiety == add_point(socialAnxiety)
                    cognition == add_point(cognition)
            elif question["type"] == "personality_b":
                if int(answer) == 0 or 1:
                    socialAnxiety = add_point(socialAnxiety)
            elif question["type"] == "personality_c":
                if int(answer) == 2 or 3:
                    inattention = add_point(inattention)
            elif question["type"] == "personality_d":
                if int(answer) == 2 or 3:
                    lackOfEmpathy = add_point(lackOfEmpathy)
                    cognition == add_point(cognition)
            elif question["type"] == "personality_e":
                if int(answer) == 0 or 1:
                    lackOfEmpathy = add_point(lackOfEmpathy)
                    inattention = add_point(inattention)
            elif question["type"] == "personality_f":
                if int(answer) == 0 or 1:
                    lackOfEmpathy = add_point(lackOfEmpathy)
            elif question["type"] == "personality_g":
                if int(answer) == 2 or 3:
                    socialAnxiety = add_point(socialAnxiety)
            elif question["type"] == "personality_h":
                if int(answer) == 0 or 1:
                    inattention = add_point(inattention)
            elif question["type"] == "personality_i":
                if int(answer) == 0 or 1:
                    socialAnxiety == add_point(socialAnxiety)
                    cognition == add_point(cognition)
            elif question["type"] == "personality_j":
                if int(answer) == 0 or 1:
                    cognition == add_point(cognition)
        result = judge(socialAnxiety, lackOfEmpathy, inattention, cognition)
        return render_template("quiz_b/question_b.html", result=result, questions=questions, questions_with_index=questions_with_index, socialAnxiety=socialAnxiety, 
            lackOfEmpathy=lackOfEmpathy, inattention=inattention, cognition=cognition)
    
    #初期化またはGETリクエストのとき
    socialAnxiety = 0
    lackOfEmpathy = 0
    inattention =0 
    cognition =0
    return render_template("quiz_b/question_b.html", questions=questions, questions_with_index=questions_with_index, socialAnxiety=socialAnxiety, 
        lackOfEmpathy=lackOfEmpathy, inattention=inattention, cognition=cognition, result=None)
