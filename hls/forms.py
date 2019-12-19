from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed


class AudioForm(FlaskForm):
    audio = FileField('Audio', FileRequired(), FileAllowed(['wav']))
    submit = SubmitField('Submit')

