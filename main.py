from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8d391fa09d0b74fb0dde2c7c072aebb0'

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dannynguyen312@gmail.com' and form.password.data == 'Nguyen0210':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

if __name__ == '__main__':
    app.run(debug=True)