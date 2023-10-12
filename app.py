import os
from flask import render_template, request, redirect, session
from sqlalchemy import text, desc
from Models import Users, Recipe, Role
from config import app, db, DEFAULT_USER_PHOTO, PATH_USER_PHOTO, PATH_RECIPE_PHOTO, \
    PATH_TO_PROJECT, SEARCH_QUERY_SQL, SEARCH_CATEGORY_QUERY_SQL
from scripts import allowed_file
from werkzeug.utils import secure_filename


# страница с рецептами
@app.route('/', methods=['POST', 'GET'])
def index():

    categories = Recipe.query.with_entities(Recipe.category).distinct()

    if 'isSignIn' not in session:
        session['isSignIn'] = False
        session['id_user'] = None
        session['username'] = None

    recipes = Recipe.query \
        .join(Users, Recipe.id_user == Users.id_user) \
        .add_columns(Recipe.id_recipe, Recipe.description, Recipe.name_recipe, Recipe.recipe,
                     Recipe.id_user, Recipe.recipe_photo, Recipe.category, Users.nickname) \
        .order_by(desc(Recipe.id_recipe)).all()

    if request.method == "POST":

        search_text = request.form.get('search_text')
        category = request.form.get('categ')

        if category == "категория":
            recipes = db.session.execute(text(SEARCH_QUERY_SQL), {"search_text": search_text})\
                .all()
        else:
            recipes = db.session\
                .execute(text(SEARCH_CATEGORY_QUERY_SQL), {"search_text": search_text, "category": category})\
                .all()

        print(category)

    return render_template("main.html", isSignIn=session['isSignIn'], nickname=session['username'], recipes=recipes,
                           id_user=session['id_user'], categories=categories)


# Инфа о нас
@app.route('/about')
def about():
    return render_template("about.html", isSignIn=session['isSignIn'], nickname=session['username'])


# вход
@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if session['username'] is not None:
        return redirect('/')

    users = Users.query.all()

    if request.method == "POST":
        nickname: str = request.form.get('nickname')
        password: str = request.form.get('password')

        for user in users:
            if nickname == user.nickname and password == user.password:
                session.pop('username')
                session['username'] = nickname
                session.pop('id_user')
                session['id_user'] = user.id_user
                session.pop('isSignIn')
                session['isSignIn'] = True

                print("Вошли")
                print(session['id_user'])
                return redirect(f"/profile+{session['username']}")

        print("Не вошли")

    return render_template("sign_in.html", isSignIn=session['isSignIn'], nickname=session['username'])


# регистрация
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        nickname: str = request.form.get('nickname')
        email: str = request.form.get('email')
        password: str = request.form.get('password')
        repPassword: str = request.form.get('repeatedPassword')

        if password == repPassword:
            users = Users.query.all()
            for u in users:
                if email == u.email or nickname == u.nickname:
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
    count_of_recipes = Recipe.query \
        .join(Users, Recipe.id_user == Users.id_user) \
        .add_columns(Users.nickname, Recipe.id_recipe, Recipe.description, Recipe.name_recipe, Recipe.recipe,
                     Recipe.id_user) \
        .filter_by(nickname=profile_nickname) \
        .count()

    user_info = Users.query.filter_by(nickname=profile_nickname).first().user_info
    try:
        user_photo_name: str = Users.query.filter_by(nickname=profile_nickname).first_or_404().user_photo
        user_photo = PATH_USER_PHOTO + user_photo_name
    except TypeError as ex:
        user_photo = DEFAULT_USER_PHOTO
        print(ex)

    print(user_photo)

    profile_recipes = Recipe.query \
        .join(Users, Recipe.id_user == Users.id_user) \
        .add_columns(Users.nickname, Users.user_info, Recipe.id_recipe, Recipe.description, Recipe.name_recipe,
                     Recipe.recipe, Recipe.id_user, Recipe.recipe_photo) \
        .filter_by(nickname=profile_nickname) \
        .order_by(desc(Recipe.id_recipe)).limit(5)

    return render_template("profile.html", isSignIn=session['isSignIn'], nickname=session['username'],
                           profile_nickname=profile_nickname, count_of_recipes=count_of_recipes,
                           profile_recipes=profile_recipes, user_info=user_info, user_photo=user_photo)


@app.route('/profile+<string:profile_nickname>+all', methods=['POST', 'GET'])
def profile_all_recipes(profile_nickname):
    count_of_recipes = Recipe.query \
        .join(Users, Recipe.id_user == Users.id_user) \
        .add_columns(Users.nickname, Recipe.id_recipe, Recipe.description, Recipe.name_recipe, Recipe.recipe,
                     Recipe.id_user) \
        .filter_by(nickname=profile_nickname) \
        .count()

    user_info = Users.query.filter_by(nickname=profile_nickname).first().user_info
    try:
        user_photo_name: str = Users.query.filter_by(nickname=profile_nickname).first_or_404().user_photo
        user_photo = PATH_USER_PHOTO + user_photo_name
    except TypeError as ex:
        user_photo = DEFAULT_USER_PHOTO
        print(ex)

    profile_recipes = Recipe.query \
        .join(Users, Recipe.id_user == Users.id_user) \
        .add_columns(Users.nickname, Recipe.id_recipe, Recipe.description, Recipe.name_recipe, Recipe.recipe,
                     Recipe.id_user, Recipe.recipe_photo) \
        .filter_by(nickname=profile_nickname) \
        .order_by(desc(Recipe.id_recipe)).all()
    return render_template("profile.html", isSignIn=session['isSignIn'], nickname=session['username'],
                           profile_nickname=profile_nickname,
                           count_of_recipes=count_of_recipes, profile_recipes=profile_recipes, user_info=user_info,
                           user_photo=user_photo)


@app.route('/exit')
def exit():
    session.pop('username')
    session['username'] = None
    session.pop('id_user')
    session['id_user'] = None
    session.pop('isSignIn')
    session['isSignIn'] = False

    return redirect("/")


@app.route('/recipe+<int:id_recipe>')
def recipe(id_recipe):
    recipe = Recipe.query.filter_by(id_recipe=id_recipe).first()
    return render_template("recipe.html", isSignIn=session['isSignIn'], nickname=session['username'], recipe=recipe)


@app.route('/new_recipe', methods=['POST', 'GET'])
def new_recipe():
    if request.method == "POST":
        name_recipe: str = request.form.get('name_recipe')
        description: str = request.form.get('description')
        recipe: str = request.form.get('recipe').replace("\n", "<br />")
        category: str = request.form.get('categ')

        file = request.files['file']
        recipe_photo = secure_filename(file.filename)

        if recipe_photo == "":
            recipe_photo = ""
        else:
            file.save(PATH_TO_PROJECT + PATH_RECIPE_PHOTO + recipe_photo)

        recipe = Recipe(name_recipe=name_recipe, description=description, recipe=recipe, id_user=session['id_user'],
                        recipe_photo=recipe_photo, category=category)
        if name_recipe != "":
            try:
                db.session.add(recipe)
                db.session.commit()
                return redirect(f"/profile+{session['username']}")
            except Exception as e:
                print(e)

    return render_template("new_recipe.html", isSignIn=session['isSignIn'], nickname=session['username'])


@app.route('/new_info', methods=['POST', 'GET'])
def new_info():
    user = Users.query.filter_by(id_user=session['id_user']).first()

    if request.method == "POST":



        nickname: str = request.form.get('nickname')

        print(nickname)
        email: str = request.form.get('email')

        password: str = request.form.get('password')
        repPassword: str = request.form.get('repeatedPassword')

        user_info: str = request.form.get('user_info')


        file = request.files['file']
        user_photo: str = secure_filename(file.filename)

        if password == repPassword:

            if nickname != user.nickname or email != user.email:

                users = Users.query.all()
                for u in users:
                    if email == u.email or nickname == u.nickname:
                        print("Занято 2")
                        return redirect('/sign_up')

            try:
                if nickname == "":
                    nickname: str = user.nickname
                if email == "":
                    email = user.email
                if repPassword == "" or password == "":
                    password = user.password
                    repPassword = user.password
                if user_info == "":
                    user_info = user.user_info
                if user_photo == "":
                    user_photo = user.user_photo
                else:
                    file.save(PATH_TO_PROJECT+PATH_USER_PHOTO+secure_filename(file.filename))

                user.nickname = nickname
                user.email = email
                user.password = password
                user.user_info = user_info
                user.user_photo = user_photo
                db.session.commit()

                session.pop('username')
                session['username'] = nickname

                return redirect(f"/profile+{session['username']}")
            except Exception as e:
                print(e)
        else:
            print("Пароли не совпадают")
    return render_template("new_info.html", isSignIn=session['isSignIn'], nickname=session['username'], user=user)


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
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
