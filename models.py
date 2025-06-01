from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#更新情報データベース
class NewRelease(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=False)

#管理者用データベース
class User(db.Model):
    __bind_key__ = 'user_management'  # Specify the secondary database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)