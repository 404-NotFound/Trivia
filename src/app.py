#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask,render_template,redirect,url_for,session,send_from_directory
from models.trivia import Categoria,Pregunta,Respuesta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy.sql.expression import func
from datetime import datetime, timedelta
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5ac358cf0bf-11e5-9e39-d3b532c10a28' #or os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///models/trivia.db'
db= SQLAlchemy(app)

@app.route('/')
def index():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia')
def trivia_inicio():
    session.clear()
    return render_template("index.html.jinja2",titulo="")

@app.route('/trivia/')
def trivia_inicio2():
    return redirect(url_for('trivia_inicio'))

@app.route('/trivia/categorias')
def trivia_categorias():
    
    #LE PIDO TODAS LAS CATEGORIAS A Categorias
    todas_categorias=Categoria.query.all()
    
    #CREO SESSION['ti']=<TIEMPO> SESSION['ID_CATEGORIA']=<TRUE O FALSE>
    #GUARDO EN ELLA SI GANO O PERDIO CADA CATEGORIA Y EL TIEMPO QUE EMPEZO A JUGAR
    try:
        #PRIMERO COMPRUEBO SI LA SESION YA EXISTE
        if session['ti']:
            pass;
    except:
        #SI NO EXISTE CREO SESSION
        session['ti']=time.time()
        dicc = {}
        for cat in todas_categorias:
            dicc[cat.id] = False
            session[str(cat.id)] = False
    
    #DECLARO lista_ganadas QUE TIENE CADA CATEGORIA GANADA: {'nombre':<NOMBRE>}
    lista_ganadas=[]
    for ganada in todas_categorias:
        if session[str(ganada.id)] == True:
            lista_ganadas.append({
                "nombre":ganada.nombre
                })
            
    #DECLARO lista_categorias QUE POR CADA CATEGORIA TIENE UN DIC: {'nombre':<NOMBRE>,'url':<RUTA>}
    lista_categorias=[]
    for categoria in todas_categorias:
        if session[str(categoria.id)] == False:
            lista_categorias.append({
                "nombre":categoria.nombre,
                #URL_FOR ARMA LA RUTA PARA: trivia_pregunta(id_categoria)
                "url":url_for('trivia_pregunta',id_categoria=categoria.id)
                })
    
    tiempo=tiempo_jugado(session['ti'])
        
    return render_template("categorias.html.jinja2",
                           lista_categorias=lista_categorias,
                           lista_ganadas=lista_ganadas,
                           tiempo=tiempo,
                           titulo=" - Categorías")

@app.route('/trivia/<int:id_categoria>/pregunta')
def trivia_pregunta(id_categoria):
    
    #LE PIDO nombre A LA CATEGORIA QUE SE ELIGIÓ
    nombre_categoria=Categoria.query.filter_by(id=id_categoria).first().nombre
    
    #LE PIDO UNA PREGUNTA AL AZAR A LA TABLA Pregunta QUE SEA DE LA CATEGORIA QUE SE ESTA JUGANDO
    pregunta=Pregunta.query.filter_by(id_categoria=id_categoria).order_by(func.random()).first()

    #PIDO LAS RESPUESTAS PARA LA PREGUNTA ELEGIDA EN ORDEN ALEATORIO
    respuestas=Respuesta.query.filter_by(id_pregunta=pregunta.id).order_by(func.random()).all()
    
    #DECLARO lista_respuestas QUE POR CADA RESPUESTA TIENE UN DIC: {'text':<RESPUESTA>,'es_correcta':<True O False>,'url':<RUTA>}
    lista_respuestas=[]
    for respuesta in respuestas:
        lista_respuestas.append({
            "text":respuesta.text,
            "es_correcta":respuesta.es_correcta,
            #ACÁ LE ENVIO AL TEMPLATE LAS RUTAS PARA QUE CADA RESPUESTA SE DIRIGA A SU RESULTADO
            #URL_FOR ARMA LA RUTA HACIA: trivia_resultado(id_categoria,id_respuesta)
            "url":(url_for('trivia_resultado',id_categoria=id_categoria,id_respuesta=respuesta.id))
            })
        
        tiempo=tiempo_jugado(session['ti'])
        
    return render_template("pregunta.html.jinja2",
                           nombre_categoria=nombre_categoria,
                           pregunta=pregunta.text,
                           respuestas=lista_respuestas,
                           tiempo=tiempo,
                           titulo=" - Pregunta"
                           )

@app.route('/trivia/<int:id_categoria>/resultado/<int:id_respuesta>')
def trivia_resultado(id_categoria,id_respuesta):
    
    #BUSCO LA Respuesta ELEGIDA CON LA ID 
    respuesta_e=Respuesta.query.filter_by(id=id_respuesta).first()
    
    #CON LA RESPUESTA BUSCO CUAL ES LA PREGUNTA
    pregunta=Pregunta.query.filter_by(id=respuesta_e.id_pregunta).first()
    
    #PIDO LAS 3 RESPUESTAS PARA LA PREGUNTA ELEGIDA POR ORDEN DECRECIENTE
    respuestas=Respuesta.query.filter_by(id_pregunta=pregunta.id).order_by(desc(Respuesta.es_correcta)).all()
    
    #DECLARO lista_respuestas QUE POR CADA RESPUESTA TIENE UN DIC: {'text':<RESPUESTA>,'es_correcta':<True O False>,'url':<RUTA>}
    lista_respuestas=[]
    for respuesta in respuestas:
        lista_respuestas.append({
            "id":respuesta.id,
            "text":respuesta.text,
            "es_correcta":respuesta.es_correcta
            })
        
    # esto es para setear en la session si acierta o no la pregunta
    for respuesta in respuestas:
        if respuesta.es_correcta:
            if respuesta.id == id_respuesta:
                session[str(id_categoria)] = True
     
    todas_categorias=Categoria.query.all()
    ganador = True
    for c in todas_categorias:
        if session[str(c.id)] == False:
            ganador = False
    if ganador==True:
        return redirect(url_for('trivia_fin'))
    
    url_perdio=url_for('trivia_pregunta',id_categoria=id_categoria)
    url_gano=url_for('trivia_categorias')
    
    #LA FUNCION TIEMPO JUGADO DEVUELVE LA RESTA DE TI-TF FORMATEADA EN TEXTO
    tiempo=tiempo_jugado(session['ti'])
        
    return render_template("resultado.html.jinja2",
                           pregunta=pregunta.text,
                           respuestas=lista_respuestas,
                           resultado=respuesta_e.es_correcta,
                           relegida=respuesta_e.text,
                           url_gano=url_gano,
                           url_perdio=url_perdio,
                           tiempo=tiempo,
                           titulo=" - Respuesta"
                           )
    
@app.route('/trivia/fin')
def trivia_fin():
    #LA FUNCION TIEMPO JUGADO DEVUELVE LA RESTA DE TI-TF FORMATEADA EN TEXTO
    tiempo=tiempo_jugado(session['ti'])
    
    return render_template("fin.html.jinja2", tiempo=tiempo, titulo=" - Fin")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static'),'favicon/favicon.ico', mimetype='image/vnd.microsoft.icon')

def tiempo_jugado(ti):
    tf=time.time()
    duracion=tf-ti
    formato=datetime(1,1,1)+(timedelta(seconds=int(duracion)))
    if formato.hour>0:
        return "%d horas, %d minutos y %d segundos" % (formato.hour, formato.minute, formato.second)
    else:
        return "%d minutos y %d segundos" % (formato.minute, formato.second)
