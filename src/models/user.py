#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,redirect,url_for,session
from models.trivia import Usuario, Post
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5ac358cf0bf-11e5-9e39-d3b532c10a28' #or os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///models/trivia.db'
db = SQLAlchemy(app)

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired("Ingrese su nombre de usuario.")])
    password = PasswordField('Contraseña', validators=[DataRequired("Debe ingresar su contraseña.")])
    submit = SubmitField('Entrar')
    
class RegisterForm(FlaskForm):
    username = StringField("Nombre", [DataRequired("Debe ingresar un nombre de usuario.")])
    password = PasswordField('Contraseña', validators=[DataRequired("La contraseña debe contener almenos 6 caracteres.")])
    password_repeat = PasswordField('Repetir contraseña', validators=[DataRequired("La contraseña es distinta.")])
    email = EmailField("Email", [DataRequired("Por favor, ingrese su dirección mail."), Email("Debe ingresar un mail válido.")])
    submit = SubmitField('Registrar')

class MessageForm(FlaskForm):
    username = StringField("Autor", [DataRequired("Debe ingresar un usuario.")])
    email = EmailField("Email", [DataRequired("Por favor, ingrese su dirección mail."), Email("Debe ingresar un mail válido.")])
    message = TextAreaField("Mensaje", [DataRequired("Escriba aquí su mensaje.")])
    submit = SubmitField('Registrar')

@app.route('/trivia/login', methods=['GET', 'POST'])
def login():
        
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('user'))
    
        try:
            if session['user_id']:
                pass;
        except:
            session['ti']=time.time()
        
    return render_template('login.html.jinja2', form=form)

@app.route('/trivia/registrarme', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('User registred {}, email={}'.format(
            form.username.data, form.email.data))
        return redirect(url_for('login'))
    return render_template('register.html.jinja2', form=form)

@app.route('/usuario')
def user():
    session['user_id']=1
    try:
        if session['user_id']:
            pass;
    except:
        return redirect(url_for('login'))
        
    id_s=session['user_id']
    user=Usuario.query.filter_by(id=id_s).first()
    print(str(user))
    print(str(user.id),str(user.username),str(user.email),str(user.ganadas),str(user.mejor_tf))
    usuario={
            'id':user.id,
            'nombre':user.username,
            'email':user.email,
            'ganadas':user.ganadas,
            'mejor_tf':user.mejor_tf
            }
    return render_template('user.html.jinja2',usuario=usuario)

@app.route('/salir')
def salir():
    session.clear()
    return redirect(url_for('index'))
    