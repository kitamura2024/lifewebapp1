from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class NewReleaseForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired(), Length(max=100)])
    date = StringField('日付 (YYYY-MM-DD)', validators=[DataRequired(), Length(max=10)])
    description = TextAreaField('説明', validators=[DataRequired()])
    submit = SubmitField('保存')
