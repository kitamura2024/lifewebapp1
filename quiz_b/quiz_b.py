from flask import Blueprint, render_template, request, url_for

#Blueprintを定義
quiz_bp = Blueprint('quiz_b', __name__, template_folder='../templates')

#初期化
simple = 0
multitask = 0
steadily = 0
forgetWord = 0
quick = 0
forgetAction = 0
forgetItem = 0
planning = 0
time = 0 
anxiety =0 
careless =0

def add_point(x):
    return x + 1

def judge(simple, multitask, steadily, forgetWord, quick, forgetAction, forgetItem,
          planning, time, anxiety, careless):
    if int(time) >= 3:
        return "あなたは単純作業や同じことの繰り返しの作業が苦手な傾向があるようです。\nあなたにオススメな生活の工夫・対策の例は以下のようなものです。"
    else:
        return "苦手な傾向は今回の結果からは見当たりませんでした。他の診断をお試しいただくか、生活の工夫・対策の一覧から気になるものを試してみてください。"

questions = [
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_a"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
    {"question": "『やるべきことや予定を忘れることがある』", "options": ["そう思う", "ややそう思う", "あまりそう思わない", "そう思わない"], "type": "personality_b"},
]
questions_with_index = list(enumerate(questions))  # インデックス付きリストを作成

@quiz_bp.route("/quiz_b", methods=["GET", "POST"])
def quiz():
    global simple, multitask, steadily, forgetWord, quick, forgetAction, forgetItem, planning, time, anxiety, careless
    if request.method == "POST":
        for i, question in enumerate(questions):
            answer = request.form.get(f"q{i+1}") #回答した値を取得
            if not answer:
                continue

            #ポイントの加算
            if question["type"] == "personality_a":
                if int(answer) == 1:#整数値1のとき
                    simple = add_point(simple)
                elif int(answer) == 2:
                    multitask = add_point(multitask)
            elif question["type"] == "personality_b":
                if int(answer) == 1:
                    time = add_point(time)

        result = judge(simple, multitask, steadily, forgetWord, quick, forgetAction, forgetItem,
               planning, time, anxiety, careless)
        return render_template("quiz_b/question_b.html", result=result, questions=questions, questions_with_index=questions_with_index, simple=simple, multitask=multitask, steadily=steadily, forgetWord=forgetWord, quick=quick, forgetAction=forgetAction, forgetItem=forgetItem,
          planning=planning, time=time, anxiety=anxiety, careless=careless)
    
    #初期化またはGETリクエストのとき
    simple = 0
    multitask = 0
    steadily = 0
    forgetWord = 0
    quick = 0
    forgetAction = 0
    forgetItem = 0
    planning = 0
    time = 0 
    anxiety =0 
    careless =0
    return render_template("quiz_b/question_b.html", questions=questions, questions_with_index=questions_with_index, simple=simple, multitask=multitask, steadily=steadily, forgetWord=forgetWord, quick=quick, forgetAction=forgetAction, forgetItem=forgetItem,
          planning=planning, time=time, anxiety=anxiety, careless=careless, result=None)
