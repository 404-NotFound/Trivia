from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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