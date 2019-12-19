from flask import render_template, url_for, redirect
import os.path
import sys

from hls import app
from hls.forms import AudioForm
from hls.offline_wav import compute


@app.route("/", methods=['GET','POST'])
def home():
    form = AudioForm()
    if form.validate_on_submit():
        f = form.audio.data
        f.save('input.wav')
        return redirect(url_for('output'))
    return render_template('home.html', title='Home', form=form)


@app.route("/output")
def output():
    compute("input.wav", "output.wav")
    return render_template(
        'output.html',
        title='Output',
        file=output_file
    )