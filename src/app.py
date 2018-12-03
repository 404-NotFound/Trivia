#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
from flask import send_from_directory
'''
from flask import Flask, render_template, redirect, url_for
from models.trivia import db, Categoria, Pregunta, Respuesta
from flask_sqlalchemy import SQLAlchemy
from  sqlalchemy.sql.expression import func, select

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///models/trivia.db'
db= SQLAlchemy(app)

@app.route('/')
def trivia_():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia')
def trivia_inicio():
    return render_template("index.html.jinja2")

@app.route('/trivia/')
def trivia_inicio2():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia/categorias')
def trivia_categorias():
    #LE PIDO TODAS LAS CATEGORIAS A Categorias
    todas_categorias=Categoria.query.all()
    lista_categorias=[]
    #LE PASO AL TEMPLATE UNA LISTA QUE POR CADA CATEGORIA TIENE UN DIC CON: NOMBRE, RUTA.
    for categoria in todas_categorias:
        lista_categorias.append({
            "nombre":categoria.nombre,
            #URL ARMA LA RUTA QUE VA A trivia_pregunta
            "url":url_for('trivia_pregunta',id_categoria=categoria.id)
            })
    return render_template("categorias.html.jinja2",lista_categorias=lista_categorias)

@app.route('/trivia/<int:id_categoria>/pregunta')
def trivia_pregunta(id_categoria):
    #LE PIDO EL NOMBRE DE LA CATEGORIA A LA TABLA Categoria
    q_categoria=Categoria.query.filter_by(id=id_categoria).first()
    nombre_categoria=q_categoria.nombre    
    #LE PIDO UNA PREGUNTA AL AZAR A LA TABLA Pregunta
    pregunta_random=Pregunta.query.filter_by(categoria_id=id_categoria).order_by(func.random()).first()
    pregunta=pregunta_random.text
    pregunta_id=pregunta_random.id    
    #LE PIDO LAS RESPUESTAS EN ORDEN ALEATORIO A LA TABLA Respuestas
    q_respuestas=Respuesta.query.filter_by(pregunta_id=pregunta_id).order_by(func.random()).all()
    #LE PASO AL TEMPLATE UNA LISTA QUE POR CADA RESPUESTA TIENE UN DIC CON: RESPUESTA, SI ES CORRECTA, RUTA.
    lista_respuestas=[]
    for respuesta in q_respuestas:
        lista_respuestas.append({
            "text":respuesta.text,
            "es_correcta":respuesta.es_correcta,
            #URL ARMA LA RUTA QUE VA A trivia_resultado
            "url":url_for('trivia_resultado',id_categoria=id_categoria,id_respuesta=respuesta.id)
            })
    return render_template("pregunta.html.jinja2",nombre_categoria=nombre_categoria,pregunta=pregunta,respuestas=lista_respuestas)

@app.route('/trivia/<int:id_categoria>/resultado/<int:id_respuesta>')
def trivia_resultado(id_categoria,id_respuesta):
    return render_template("resultado.html.jinja2")

@app.route('/trivia/fin')
def trivia_fin():
    return render_template("fin.html.jinja2")
