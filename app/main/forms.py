from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired

from .defs import candidates

blank_option = ('', ' -- select an option -- ')


class VotingForm(FlaskForm):
    selection = SelectField('投票',
                            choices=[blank_option] + candidates,
                            validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('提交')
