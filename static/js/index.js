const questions = [
    {
        question: "『やるべきことや予定を忘れることがある』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 3, forgetItem: 1, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 2, forgetItem: 1, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    {
        question: "『同じことの繰り返しや単純な作業が続くと、疲れやすいまたは集中が途切れやすい』",
        answers: [
            { text: "そう思う", points: { simple: 3, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 3 } },
            { text: "ややそう思う", points: { simple: 2, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 2 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    {
        question: "『予定していた時間に遅れることはほとんどない』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: -1, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: -1, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 1, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 2, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 1, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 3, anxiety: 0, careless: 0 } }
        ]
    },
    {
        question: "『複数の指示を一度に受けると混乱することがある』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 2, steadily: 0, forgetWord: 3, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 1, steadily: 0, forgetWord: 2, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    {
        question: "『傘やスマートフォン等、ものをどこかに置き忘れることがある』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 3, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 2, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    {
        question: "『複数の作業を同時に進めていくことが好きだ』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 2, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 1, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 3, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 1, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    {
        question: "『完了した作業に間違いがないか何度も確認をする』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 3, careless: 1 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 2, careless: 1 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    { 
        question: "『何か行動するとき、自分で時間を決めて時間通りに行動することができる』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 2, time: 1, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 3, time: 2, anxiety: 0, careless: 0 } }
        ]
    },
    { 
        question: "『割とテキパキ動くことができる』",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 2, steadily: 0, forgetWord: 0, quick: 3, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 1, steadily: 0, forgetWord: 0, quick: 2, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    { 
        question: "『パズルや謎解きゲームのようにじっくりと考えたり推理したりすることが好きだ』",
        answers: [
            { text: "そう思う", points: { simple: 1, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 1, time: 0, anxiety: 0, careless: 0 } }
        ]
    },
    /* { 
        question: "やるべきことや予定を忘れることがある",
        answers: [
            { text: "そう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "ややそう思う", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "あまりそう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } },
            { text: "そう思わない", points: { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 } }
        ]
    }, */
    // 他の質問も同様に追加
];

function displayQuestions() {
    const questionContainer = document.getElementById('questions');
    questions.forEach((q, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.innerHTML = `<p>${q.question}</p>`;
        q.answers.forEach((answer, i) => {
            questionDiv.innerHTML += `
                <input type="radio" name="question${index}" value="${i}">
                <label>${answer.text}</label><br>
            `;
        });
        questionContainer.appendChild(questionDiv);
    });
}

function calculateResults() {
    const results = { simple: 0, multitask: 0, steadily: 0, forgetWord: 0, quick: 0, forgetAction: 0, forgetItem: 0, planning: 0, time: 0, anxiety: 0, careless: 0 };
    questions.forEach((q, index) => {
        const selectedAnswer = document.querySelector(`input[name="question${index}"]:checked`);
        if (selectedAnswer) {
            const answerPoints = q.answers[selectedAnswer.value].points;
            results.simple += answerPoints.simple;/* resultsオブジェクトのkindnessに加える */
            results.multitask += answerPoints.multitask;
            results.steadily += answerPoints.steadily;
            results.forgetWord += answerPoints.forgetWord;
            results.careless += answerPoints.careless;
            results.quick += answerPoints.quick;
            results.forgetAction += answerPoints.forgetAction;
            results.forgetItem += answerPoints.forgetItem;
            results.planning += answerPoints.planning;
            results.anxiety += answerPoints.anxiety;
            results.time += answerPoints.time;
        }
    });
    displayResults(results);
}

function displayResults(results) {
    const resultContainer = document.getElementById('results');
    
    resultContainer.innerHTML = `
        <p>単純作業が苦手（集中力がない）締め切りのある状況が苦手: ${results.simple}</p>
        <p>マルチタスクが苦手: ${results.multitask}</p>
        <p>コツコツ続けることが苦手（長続きしない）: ${results.steadily}</p>
        <p>聞いたことを忘れる: ${results.forgetWord}</p>
        <p>やるべきことをよく忘れる、聞いたことを忘れる: ${results.forgetAction}</p>
        <p>不安になりやすい: ${results.anxiety}</p>
        <p>新しいことに取り組む、問題解決方法を自ら見つける、発想力（料理を考える）、収納や整理整頓: ${results.quick}</p>
        <p>時間の管理が苦手: ${results.time}</p>
        <p>プランニング（行動の計画を立てること、優先順位）、片付けをやり始める、締め切り苦手: ${results.planning}</p>
        <p>物をよく忘れる: ${results.forgetItem}</p>
        <p>集中が続かない、単純作業が苦手: ${results.careless}</p>
        


    `;
    if (results.simple >= 3) {
        document.getElementById("resultMessage").innerText = "あなたは単純作業や同じことの繰り返しの作業が苦手な傾向があるようです。あなたにオススメな生活の工夫・対策の例は以下のようなものです。";
    } else if(results.multitask >= 3) {
        document.getElementById("resultMessage").innerText = "あなたは複数のことを同時に行うようなマルチタスク作業が苦手な傾向があるようです。あなたにオススメな生活の工夫・対策の例は以下のようなものです。";
    } else {
        document.getElementById("resultMessage").innerText = "苦手な傾向は今回の結果からは見当たりませんでした。他の診断をお試しいただくか、生活の工夫・対策の一覧から気になるものを試してみてください。";
    }

}



function showMessage() {
    document.getElementById('message').innerText = 
    '過去２週間にどのように感じたか、以下の質問に答えてください。\n回答の際はあまり考えこまず、率直に思った選択肢を選んでください。';
}

window.onload = displayQuestions;
