from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Miguel'}
    posts = [
        {
            'author' : {'username' : 'john'},
            'body' : "Everyone's life got ups and downs, just never stop moving forward"
        },
        {
            'author' : {'username' : 'barca_fc'},
            'body' : 'great day for the Madrid'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign in', form=form)