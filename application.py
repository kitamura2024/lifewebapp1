from flask import Flask, render_template, url_for, redirect, flash, request
from quiz_b.quiz_b import quiz_bp
from quiz_a.quiz_a import quiz_bp_a
from models import db, NewRelease, User
from wtf import NewReleaseForm
from login import is_login, try_login, try_logout

app = Flask(__name__)

app.register_blueprint(quiz_bp)#Blueprintを登録
app.register_blueprint(quiz_bp_a)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_BINDS'] = {
    'user_management': 'sqlite:///user_management.db'  # Secondary database for user management
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jou8oauien2koiu4jinmklmoui09jpwoio3lm'#開発用
db.init_app(app)

# 初回起動時にデータベースを初期化
with app.app_context():
    db.create_all()
###
# 管理者ページ：リリース一覧
@app.route('/admin/releases')
def admin_releases():
    releases = NewRelease.query.all()
    return render_template('new_releases/admin_releases.html', releases=releases)

# 管理者ページ：新規リリース作成
@app.route('/admin/releases/new', methods=['GET', 'POST'])
def new_release():
    form = NewReleaseForm()
    if form.validate_on_submit():
        release = NewRelease(
            title=form.title.data,
            date=form.date.data,
            description=form.description.data
        )
        db.session.add(release)
        db.session.commit()
        flash('新しいリリースを作成しました！')
        return redirect(url_for('admin_releases'))
    return render_template('new_releases/new_releases.html', form=form)

# 管理者ページ：リリース編集
@app.route('/admin/releases/edit/<int:release_id>', methods=['GET', 'POST'])
def edit_release(release_id):
    release = NewRelease.query.get_or_404(release_id)
    form = NewReleaseForm(obj=release)
    if form.validate_on_submit():
        release.title = form.title.data
        release.date = form.date.data
        release.description = form.description.data
        db.session.commit()
        flash('リリースを更新しました！')
        return redirect(url_for('admin_releases'))
    return render_template('new_releases/edit_releases.html', form=form, release=release)

# 管理者ページ：リリース削除
@app.route('/admin/releases/delete/<int:release_id>', methods=['POST'])
def delete_release(release_id):
    release = NewRelease.query.get_or_404(release_id)
    db.session.delete(release)
    db.session.commit()
    flash('リリースを削除しました！')
    return redirect(url_for('admin_releases'))

# 管理者ページ：ログイン
@app.route('/login')
def login_page():
    return render_template('login/login.html')

@app.route('/check_login', methods=['POST'])
def check_login():
    user, pw = request.form.get('user'), request.form.get('pw')
    if not user or not pw:
        return redirect('/login')
    if not try_login(user, pw):
        return render_template('login/check_login_error.html')
    return redirect('/admin/releases')

@app.route('/logout')
def logout_page():
    try_logout()
    return render_template('login/logout.html')
# 管理者ページ：登録
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login/register.html')
    
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('pw')
        
        # 入力チェック
        if not username or not password:
            return """
            <h1>すべてのフィールドを入力してください</h1>
            <p><a href="/register">戻る</a></p>
            """
        
        # 同じ名前のユーザーが既に存在するか確認
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return """
            <h1>ユーザー名は既に使用されています</h1>
            <p><a href="/register">戻る</a></p>
            """
        
        # 新しいユーザーをデータベースに追加
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return """
        <h1>登録が完了しました！</h1>
        <p><a href="/">ログインページに戻る</a></p>
        """
###

@app.route('/')#Topページ
def top():
    new_releases = NewRelease.query.order_by(NewRelease.date.desc())
    return render_template('top.html', new_releases=new_releases)

@app.route('/purpose')#「本サイトについて」
def purpose():
    return render_template('list.html')

@app.route('/nigate_a1/')# 「準備中」
def nigate_a1():
    return render_template('nigate_a1.html')
@app.route('/nigate_a2/')#「置き忘れ」
def nigate_a2():
    return render_template('nigate_a2.html')
@app.route('/nigate_a3')#「遅刻」
def nigate_a3():
    return render_template('nigate_a3.html')

if __name__ == '__main__':
    app.run(debug=True)
