from flask_wtf import Form
from wtforms import StringField
from wtforms import SubmitField
from wtforms import RadioField
from wtforms.validators import DataRequired


class VotingForm(Form):
    selection = RadioField('投票',
                           choices=[],
                           validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('提交')
