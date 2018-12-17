#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired("Ingrese su nombre de usuario.")])
    password = PasswordField('Contraseña', validators=[DataRequired("Debe ingresar su contraseña.")])
    submit = SubmitField('Entrar')
    
class RegisterForm(FlaskForm):
    username = StringField("Nombre", [DataRequired("Debe ingresar un nombre de usuario.")])
    password = PasswordField('Contraseña', validators=[DataRequired("La contraseña debe contener almenos 6 caracteres.")])
    password_repeat = PasswordField('Repetir contraseña', validators=[DataRequired("La contraseña es distinta.")])
    email = EmailField("Email", [DataRequired("Por favor, ingrese su dirección mail."), Email("Debe ingresar un mail válido.")])
    submit = SubmitField('Registrarme')

class MessageForm(FlaskForm):
    username = StringField("Autor", [DataRequired("Debe ingresar un usuario.")])
    email = EmailField("Email", [DataRequired("Por favor, ingrese su dirección mail."), Email("Debe ingresar un mail válido.")])
    message = TextAreaField("Mensaje", [DataRequired("Escriba aquí su mensaje.")])
    submit = SubmitField('Enviar')

'''
#@app.route('/trivia/login', methods=['GET', 'POST'])
def login():
        
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('user'))

    return render_template('login.html.jinja2', login_form=login_form)

#@app.route('/usuario')
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

#@app.route('/salir')
def salir():
    session.clear()
    return redirect(url_for('index'))
'''