from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///trivia.db'
db= SQLAlchemy(app)

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    def __repr__(self):        
        return '<Categoria: %s>' % self.nombre
    
class Preguntas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), unique=True, nullable=False)
    def __repr__(self):        
        return '<Pregunta: %s>' % self.text
    
class Respuestas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), unique=True, nullable=False)
    def __repr__(self):        
        return '<Respuesta: %s>' % self.text