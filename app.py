from flask import Flask,request,render_template
from stories import story
# from flask_debugtoolbar import DebugToolbarExtension

FLASK_ENV="development"
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)


@app.route('/')
def get_Words():
    prompts=story.prompts

    return render_template('form.html',words=prompts)

@app.route('/story')
def make_story():
    text = story.generate(request.args)

    return render_template('story.html',text=text)