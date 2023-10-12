from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT
from config import app, db


class Recipe(db.Model):
    id_recipe = db.Column(db.Integer, primary_key=True)
    name_recipe = db.Column(db.String(255), nullable=False)
    recipe = db.Column(LONGTEXT)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))
    description = db.Column(db.String(250), nullable=False)
    recipe_photo = db.Column(db.String(255))
    category = db.Column(db.String(45), nullable=False)


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
    user_info = db.Column(db.String(255), nullable=True)
    user_photo = db.Column(db.String(255))

    rel_recipe = db.relationship('Recipe', backref='num_user')