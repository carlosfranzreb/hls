from flask import render_template, url_for, redirect
import os.path

from hls import app
from hls.forms import AudioForm
from hls.offline_wav import compute


@app.route("/", methods=['GET','POST'])
def home():
    form = AudioForm()
    if form.validate_on_submit():
        f = form.audio.data
        f.save(os.path.join(
            app.instance_path, 'static/audio', 'input.wav'
        ))
        return redirect(url_for('output'))
    return render_template('home.html', title='Home', form=form)


@app.route("/output")
def output():

    output_file = open("output.wav","w+")  # TODO: w+ or w?
    compute(input_file, output_file)
    return render_template(
        'output.html', 
        title='Output',
        file=output_file
    )