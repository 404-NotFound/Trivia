#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
from flask import send_from_directory
'''
from flask import Flask, request, render_template, redirect, url_for
from models.trivia import db, Categoria, Pregunta, Respuesta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///models/trivia.db'
db= SQLAlchemy(app)

@app.route('/')
def trivia_():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia')
def trivia_inicio():
    return render_template("index.html")

@app.route('/trivia/categorias')
def trivia_categorias():
    todas_categorias=Categoria.query.all()
    lista_categorias=[]
    #LE PASO AL TEMPLATE UNA LISTA QUE POR CADA CATEGORIA TIENE UN DIC CON: NOMBRE Y RUTA DE CADA UNA
    for categoria in todas_categorias:
        lista_categorias.append({
            "nombre":categoria.nombre,
            "url":url_for('trivia_pregunta',id_categoria=categoria.id)
            })
    return render_template("categorias.html",lista_categorias=lista_categorias)

@app.route('/trivia/<int:id_categoria>/pregunta')
def trivia_pregunta(id_categoria):
    consulta= Categoria.query.filter_by(id=id_categoria).first()
    categoria=consulta.nombre
    pregunta=""
    return render_template("pregunta.html",nombre_categoria=categoria,pregunta=pregunta)

@app.route('/trivia/<int:id_categoria>/resultado/<int:id_respuesta>')
def trivia_resultado(id_categoria,id_respuesta):
    return render_template("resultado.html")

@app.route('/trivia/fin')
def trivia_fin():
    return render_template("fin.html")

'''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon/favicon.ico', mimetype='image/vnd.microsoft.icon')
'''