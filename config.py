from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'osijefoi\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2802@localhost/recipes'
app.config['MAX_CONTENT_LENGTH'] = 16 * 140 * 140

db = SQLAlchemy()
db.init_app(app)

PHOTOS = '/static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['PHOTOS'] = PHOTOS

DEFAULT_USER_PHOTO = 'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-profiles/avatar-1.webp'
DEFAULT_RECIPE_PHOTO = 'https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(112).webp'
PATH_TO_PROJECT = 'C:/Users/sergm/PycharmProjects/Recipes/'
PATH_USER_PHOTO = '/static/images/users/'
PATH_RECIPE_PHOTO = '/static/images/recipes/'

SEARCH_QUERY_SQL = "select recipe.id_recipe, recipe.description, recipe.name_recipe, " \
            "recipe.recipe, recipe.id_user, recipe.recipe_photo, users.nickname, recipe.category " \
            "from recipe join users on(recipe.id_user = users.id_user) " \
            "where recipe.name_recipe like '%' :search_text '%' " \
            "or recipe.description like '%' :search_text '%' " \
            "or recipe.recipe like '%' :search_text '%' " \
            "order by recipe.id_recipe desc"

SEARCH_CATEGORY_QUERY_SQL = "select recipe.id_recipe, recipe.description, recipe.name_recipe, " \
            "recipe.recipe, recipe.id_user, recipe.recipe_photo, users.nickname, recipe.category " \
            "from recipe join users on(recipe.id_user = users.id_user) " \
            "where (recipe.name_recipe like '%' :search_text '%' " \
            "or recipe.description like '%' :search_text '%' " \
            "or recipe.recipe like '%' :search_text '%')" \
            "and recipe.category = :category " \
            "order by recipe.id_recipe desc"
