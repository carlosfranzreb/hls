from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AudioForm(FlaskForm):
    audio = FileField(validators=[FileRequired(), FileAllowed(['wav'])])
    submit = SubmitField('Submit')

