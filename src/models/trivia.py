#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, DateTime, update
from sqlalchemy.sql import exists
from flask_bcrypt import Bcrypt
from models.errors import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///trivia.db'
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    pregunta = db.relationship('Pregunta', backref='categoria',lazy='dynamic')
    def __repr__(self):        
        return '<Categoria: %s>' % self.nombre
    
class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), unique=True, nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    respuestas = db.relationship('Respuesta', backref='pregunta',lazy='dynamic')
    def __repr__(self):        
        return '<Pregunta: %s>' % self.text

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), unique=False, nullable=False)
    es_correcta = db.Column(db.Boolean, unique=False, nullable=False)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id'))
    def __repr__(self):        
        return '<Respuesta: %s>' % self.text

#EXTRAS:

class Usuario(db.Model):
    #DATOS DEL USUARIO
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    #DATOS DE TRIVIAS GANADAS
    ganadas = db.Column(db.Integer, unique=False, nullable=True)
    mejor_tf = db.Column(db.Float, unique=False, nullable=True)
    #COMENTARIOS POST
    posts = db.relationship('Post', backref='usuario',lazy='dynamic')
    #FECHA DE INGRESO
    timestamp = db.Column(DateTime(timezone=True), server_default=func.now())
    #PASSWORD ENCRIPTADO!
    password_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<User: %s>' % self.username
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    #FECHA DE PUBLICACION
    timestamp = db.Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return '<User: %s | Post: %s>' % (self.autor_id,self.text)

class Usuarie:
    def __init__(self,username,email,password,ganadas=0,mejor_tf=0.0):
        self.username = self.validarNombre(username)
        self.email = self.validarEmail(email)
        self.password = self.validarPassword(password)
        self.ganadas = self.validarGanadas(ganadas)
        self.mejor_tf = self.validarTF(mejor_tf)
    def __str__(self):
        return "Usuario: {}".format(self.username)
    def get_nombre(self):
        return self.username
    def get_email(self):
        return self.edad
    def get_ganadas(self):
        return self.ganadas
    def get_mejor_tf(self):
        return self.mejor_tf
    def validarNombre(self, v_username):
        if isinstance(v_username, str) and (4<=len(v_username)<=30):
            return v_username
        raise UserNameError()
    def validarEmail(self, v_email):
        if isinstance(v_email, str) and ("@" in v_email) and (4<=len(v_email)<=30):
            return v_email
        raise EmailError()
    def validarPassword(self, v_password):
        if isinstance(v_password, str) and (6<=len(v_password)<=128):
            return v_password
        raise PasswordInvalidaError()
    def validarGanadas(self, v_ganadas):
        if isinstance(v_ganadas, int) and v_ganadas>(-1):
            return v_ganadas
        raise TriviasGanadasError()
    def validarTF(self, v_mejor_tf):
        if isinstance(v_mejor_tf, float) and v_mejor_tf>(-1):
            return v_mejor_tf
        raise TiempoInvalidoError()
    def registrar(self):
        if db.session.query(exists().where(Usuario.username==self.username)).scalar():
            raise YaExisteUsuarioError()
        if db.session.query(exists().where(Usuario.email==self.email)).scalar():
            raise YaExisteEmailError()
        try:
            new_user = Usuario(
                username=str(self.username), 
                email=str(self.email),
                ganadas=int(self.ganadas),
                mejor_tf=float(self.mejor_tf)
                )
            new_user.set_password(str(self.password))
            db.session.add(new_user)
            db.session.commit()
            return "Usuario registrado."
        except:
            db.session.rollback()  
            raise UsuarioInvalidoError()

def logIn(username_o_mail,password):
    try:
        if "@" in username_o_mail:
            user=Usuario.query.filter_by(email=username_o_mail).first()
        else:
            user=Usuario.query.filter_by(username=username_o_mail).first()
    except:
        raise LoginError()
    if user is None:
        raise LoginUserError()
    try:
        if user.check_password(password):
            return {'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    'ganadas':user.ganadas,
                    'mejor_tf':user.mejor_tf}
    except:
        raise LoginPasswordError()
    raise LoginPasswordError()

def logOff():
    session.clear()

def postear(texto,autor_id):
    try:
        mensaje = Post(
            text=str(texto),
            autor_id=int(autor_id)
            )
        db.session.add(mensaje)
        db.session.commit()        
        return "Mensaje posteado."
    except:
        db.session.rollback()
        raise PostError()

def ganar(ganador_id):
    usuario_g=Usuario.query.filter_by(id=ganador_id).first()
    premios=usuario_g.ganadas+1    
    db.session.query(Usuario).filter(Usuario.id==ganador_id).update({'ganadas':premios})
    db.session.commit()

'''
msgP={}
try:
    p=postear("Muy bueno el juego che.", 3)
except Exception as e:
    msgP=e.to_dic()
print (msgP.get('message'),msgP.get('status_code'))

msgU={}
try:
    u=logIn("Admin","admin")
    print(u)
except Exception as e:
    msg1=e.to_dic()
print (msg1.get('message'),msg1.get('status_code'))

msgR={}
try:
    r=Usuarie("AmiguitoImaginario","amiguito@imaginario.com","amiguitomaginario").registrar()
    print(r)
except Exception as e:
    msg2=e.to_dic()
print (msg2.get('message'),msg2.get('status_code'))
'''
