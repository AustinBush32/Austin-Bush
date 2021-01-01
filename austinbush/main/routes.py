from flask import render_template, request, Blueprint


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title='Home')


@main.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')
    
@main.route('/coursework')
def coursework():
    return render_template('coursework.html', title='Coursework')