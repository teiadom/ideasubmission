from flask import Blueprint, render_template, request, redirect, url_for
#from flask_login import current_user, login_required

from flask_qa.extensions import db
from models import Idea
#from flask_qa.models import Question, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    #questions = Question.query.filter(Question.answer != None).all()

    #context = {
     #   'questions' : questions
    #}

    return render_template('home.html', **context)

@main.route('/home', methods=['GET', 'POST'])

def ask():
    if request.method == 'POST':

        what = request.form['what']
        how = request.form['how']

        question = Question(
            question=question,

        )

        db.session.add(question)
        db.session.commit()

        return redirect(url_for('main.index'))

    experts = User.query.filter_by(expert=True).all()

    context = {
        'experts' : experts
    }

    return render_template('ask.html', **context)



