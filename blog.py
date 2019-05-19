from flask import Flask, render_template, flash, url_for, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '9942cb142b266de9281ffa156d1993f0'

posts = [
    {
        'author': 'Awais Cheema',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '19 May, 2019'
    },
    {
        'author': 'Awais Cheema',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '19 May, 2019'
    }
]


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='Blog About')


@app.route('/register',methods=['GET','POST'])
def register():
    print('--------------------> Register')
    form = RegistrationForm()
    print('--------------------> Register',form.username.data)
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
