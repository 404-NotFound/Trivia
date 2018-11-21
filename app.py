#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def trivia_():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia')
def trivia_inicio():
    return render_template("trivia.html")

@app.route('/trivia/categorias')
def trivia_categorias():
    return render_template("categorias.html")

@app.route('/trivia/<int:id_categoria>/pregunta')
def trivia_pregunta(id_categoria):
    return render_template("pregunta.html",nombre_categoria="Nombre de categoria")

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
