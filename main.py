import datetime

from flask import Flask
from data import db_session
from data.users import User
from flask import render_template
from flask import redirect

from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/success')
def success():
    return render_template("success.html")


@app.route('/register', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == form.password_req.data:
            db_session.global_init("db/blogs.db")
            db_sess = db_session.create_session()
            user = User()
            user.email = form.username.data
            user.age = int(form.age.data)
            user.position = form.position.data
            user.hashed_password = str(hash(form.password.data))
            user.modified_date = datetime.datetime.now()
            user.address = form.address.data
            user.speciality = form.speciality.data
            user.name = form.name.data
            user.surname = form.surname.data
            db_sess.add(user)
            db_sess.commit()
            return redirect('/success')
    return render_template('reg.html', title="Register", form=form)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080")
