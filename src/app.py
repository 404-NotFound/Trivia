#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
from models.trivia import db, Categoria, Pregunta, Respuesta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///models/trivia.db'
db= SQLAlchemy(app)

@app.route('/')
def trivia_():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia')
def trivia_inicio():
    return render_template("trivia.html")

@app.route('/trivia/categorias')
def trivia_categorias():
    todas_categorias=Categoria.query.all()
    lista_categorias=[]
    for categoria in todas_categorias:
        lista_categorias.append({
            "nombre":categoria.nombre,
            "url":url_for('trivia_pregunta',id_categoria=categoria.id,categoria=categoria.nombre)
            })
    return render_template("categorias.html",lista_categorias=lista_categorias)

@app.route('/trivia/<int:id_categoria>/pregunta')
def trivia_pregunta(id_categoria):
    categoria=""
    return render_template("pregunta.html",categoria=categoria,pregunta="")

@app.route('/trivia/<int:id_categoria>/resultado/<int:id_respuesta>')
def trivia_resultado(id_categoria,id_respuesta):
    return render_template("resultado.html")

@app.route('/trivia/fin')
def trivia_fin():
    return render_template("fin.html")

@app.route('/nosotros')
def trivia_nosotros():
    return render_template("nosotros.html")

@app.route('/contacto')
def trivia_contacto():
    return render_template("contacto.html")