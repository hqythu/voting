from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired

blank_option = ('', ' -- select an option -- ')


class VotingForm(FlaskForm):
    selection = SelectField('投票',
                            choices=[blank_option] + [(k, v) for k, v in
                                                      current_app.candidates.items()],
                            validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('提交')
