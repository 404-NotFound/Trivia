from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, DateTime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///trivia.db'
db= SQLAlchemy(app)

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
    password_hash = db.Column(db.String(128))# ENCRIPTADO!
    #DATOS DE TRIVIAS GANADAS
    ganadas = db.Column(db.Integer, unique=False, nullable=True)
    mejor_tf = db.Column(db.Float, unique=False, nullable=True)
    #COMENTARIOS POST
    posts = db.relationship('Post', backref='usuario',lazy='dynamic')
    #FECHA DE INGRESO
    timestamp = db.Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return '<User: %s>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    #FECHA DE PUBLICACION
    timestamp = db.Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self):
        return '<User: %s | Post: %s>' % (self.autor_id,self.text)