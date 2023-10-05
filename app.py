from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT

app = Flask(__name__)
app.secret_key = b'osijefoi\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2802@localhost/recipes'

db = SQLAlchemy()
db.init_app(app)

global nick
global isSignIn
global id_user
isSignIn = False
nick = None
id_user = None


class Role(db.Model):
    id_role = db.Column(db.Integer, primary_key=True)
    name_role = db.Column(db.String(45), nullable=False)

    rel_users = db.relationship('Users', backref='num_role')


class Users(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id_role'))

    rel_recipe = db.relationship('Recipe', backref='num_user')


class Recipe(db.Model):
    id_recipe = db.Column(db.Integer, primary_key=True)
    name_recipe = db.Column(db.String(45), nullable=False)
    recipe = db.Column(LONGTEXT)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))
    description = db.Column(db.String(250), nullable=False)


# страница с рецептами
@app.route('/')
def index():
    recipes = Recipe.query\
    .join(Users, Recipe.id_user==Users.id_user)\
    .add_columns(Users.nickname, Recipe.id_recipe, Recipe.description, Recipe.name_recipe, Recipe.recipe, Recipe.id_user)\
    .all()
    return render_template("main.html", isSignIn=isSignIn, nickname=nick, recipes=recipes, id_user=id_user)

# Инфа о нас
@app.route('/about')
def about():
    return render_template("about.html", isSignIn=isSignIn, nickname=nick)

# вход
@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():

    if 'username' in session:
        return redirect('/')

    users = Users.query.all()

    if request.method == "POST":
        nickname: str = request.form.get('nickname')
        password: str = request.form.get('password')

        for user in users:
            if (nickname == user.nickname and password == user.password):
                global isSignIn
                isSignIn = True
                global nick
                nick = nickname
                global id_user
                id_user = user.id_user
                session['username'] = nickname
                print("Вошли")
                print(id_user)
                return redirect('/')

        print("Не вошли")

    return render_template("sign_in.html", isSignIn=isSignIn, nickname=nick)


# регистрация
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        nickname: str = request.form.get('nickname')
        email: str = request.form.get('email')
        password: str = request.form.get('password')
        repPassword: str = request.form.get('repeatedPassword')
        # print(nickname)

        if (password == repPassword):
            users = Users.query.all()
            for u in users:
                if (email == u.email or nickname == u.nickname):
                    print("Занято")
                    return redirect('/sign_up')

            user = Users(nickname=nickname, email=email, password=password, role=1)
            try:
                db.session.add(user)
                db.session.commit()
                return redirect('/sign_in')
            except Exception as e:
                print(e)
        else:
            print("Пароли не совпадают")
    return render_template("sign_up.html")


@app.route('/profile+<string:profile_nickname>', methods=['POST', 'GET'])
def profile(profile_nickname):
    users = Users.query.all()

    if request.method == "POST":
        return redirect('/new_recipe')

    return render_template("profile.html", isSignIn=isSignIn, nickname=nick, profile_nickname=profile_nickname)


@app.route('/exit')
def exit():
    session.pop('username')
    global nick
    nick = None
    global isSignIn
    isSignIn = False
    return redirect("/")


@app.route('/recipe+<int:id_recipe>')
def recipe(id_recipe):
    recipe = Recipe.query.filter_by(id_recipe=id_recipe).first()
    return render_template("recipe.html", isSignIn=isSignIn, nickname=nick, recipe=recipe)


@app.route('/new_recipe')
def new_recipe():

    return render_template("new_recipe.html", isSignIn=isSignIn, nickname=nick)


@app.route('/role', methods=['POST', 'GET'])
def role():
    if request.method == "POST":
        name = request.form.get('name_role')
        role = Role(name_role=name)
        try:
            db.session.add(role)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка"

    return render_template("role.html")


@app.route('/roles')
def roles():
    roles = Role.query.order_by(Role.id_role).all()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)