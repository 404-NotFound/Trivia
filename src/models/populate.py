#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.trivia import db, Categoria, Pregunta, Respuesta

#CREO TABLAS
db.drop_all()
db.create_all()

#===============================================#
#                   CATEGORIAS                  #
#===============================================#

#CREO OBJETOS
c_historia = Categoria(nombre='Historia')
c_arte = Categoria(nombre='Arte')
c_geografia = Categoria(nombre='Geografía')
c_deporte = Categoria(nombre='Deporte')

# AGREGAR A LA DB
db.session.add(c_historia)
db.session.add(c_arte)
db.session.add(c_geografia)
db.session.add(c_deporte)

db.session.commit()
#===============================================#
#           Pregunta Y RESPUETAS                #
#===============================================#

#CAPITALES:

p_capital_1 = Pregunta(text='Cuál es la capital de Paraguay', categoria=c_geografia)
r_capital_1 = Respuesta(text="Asunción", pregunta=p_capital_1)
db.session.add(p_capital_1)
db.session.add(r_capital_1)

p_capital_2 = Pregunta(text='Cuál es la capital de Argentina', categoria=c_geografia)
r_capital_2 = Respuesta(text="Buenos Aires", pregunta=p_capital_2)
db.session.add(p_capital_2)
db.session.add(r_capital_2)

p_capital_3 = Pregunta(text='Cuál es la capital de Chile', categoria=c_geografia)
r_capital_3 = Respuesta(text="Santiago de Chile", pregunta=p_capital_3)
db.session.add(p_capital_3)
db.session.add(r_capital_3)

p_capital_4 = Pregunta(text='Cuál es la capital de Brasil', categoria=c_geografia)
r_capital_4 = Respuesta(text="Brasilia", pregunta=p_capital_4)
db.session.add(p_capital_4)
db.session.add(r_capital_4)

p_capital_5 = Pregunta(text='Cuál es la capital de Venezuela', categoria=c_geografia)
r_capital_5 = Respuesta(text="Caracas", pregunta=p_capital_5)
db.session.add(p_capital_5)
db.session.add(r_capital_5)

p_capital_6 = Pregunta(text='Cuál es la capital de Bolivia', categoria=c_geografia)
r_capital_6 = Respuesta(text="La Paz", pregunta=p_capital_6)
db.session.add(p_capital_6)
db.session.add(r_capital_6)

p_capital_7 = Pregunta(text='Cuál es la capital de Uruguay', categoria=c_geografia)
r_capital_7 = Respuesta(text="Montevideo", pregunta=p_capital_7)
db.session.add(p_capital_7)
db.session.add(r_capital_7)

p_capital_8 = Pregunta(text='Cuál es la capital de Peru', categoria=c_geografia)
r_capital_8 = Respuesta(text="Lima", pregunta=p_capital_8)
db.session.add(p_capital_8)
db.session.add(r_capital_8)

p_capital_9 = Pregunta(text='Cuál es la capital de Colombia', categoria=c_geografia)
r_capital_9 = Respuesta(text="Bogotá", pregunta=p_capital_9)
db.session.add(p_capital_9)
db.session.add(r_capital_9)

p_capital_10 = Pregunta(text='Cuál es la capital de Ecuador', categoria=c_geografia)
r_capital_10 = Respuesta(text="Quito", pregunta=p_capital_10)
db.session.add(p_capital_10)
db.session.add(r_capital_10)

p_capital_11 = Pregunta(text='Cuál es la capital de México', categoria=c_geografia)
r_capital_11 = Respuesta(text="México", pregunta=p_capital_11)
db.session.add(p_capital_11)
db.session.add(r_capital_11)

p_capital_12 = Pregunta(text='Cuál es la capital de Cuba', categoria=c_geografia)
r_capital_12 = Respuesta(text="La Habana", pregunta=p_capital_12)
db.session.add(p_capital_12)
db.session.add(r_capital_12)

p_capital_13 = Pregunta(text='Cuál es la capital de Panamá', categoria=c_geografia)
r_capital_13 = Respuesta(text="Panamá", pregunta=p_capital_13)
db.session.add(p_capital_13)
db.session.add(r_capital_13)

p_capital_14 = Pregunta(text='Cuál es la capital de Portugal', categoria=c_geografia)
r_capital_14 = Respuesta(text="Lisboa", pregunta=p_capital_14)
db.session.add(p_capital_14)
db.session.add(r_capital_14)

p_capital_15 = Pregunta(text='Cuál es la capital de España', categoria=c_geografia)
r_capital_15 = Respuesta(text="Madrid", pregunta=p_capital_15)
db.session.add(p_capital_15)
db.session.add(r_capital_15)

p_capital_16 = Pregunta(text='Cuál es la capital de Francia', categoria=c_geografia)
r_capital_16 = Respuesta(text="París", pregunta=p_capital_16)
db.session.add(p_capital_16)
db.session.add(r_capital_16)

p_capital_17 = Pregunta(text='Cuál es la capital de República Dominicana', categoria=c_geografia)
r_capital_17 = Respuesta(text="Santo Domingo", pregunta=p_capital_17)
db.session.add(p_capital_17)
db.session.add(r_capital_17)

p_capital_18 = Pregunta(text='Cuál es la capital de Italia', categoria=c_geografia)
r_capital_18 = Respuesta(text="Roma", pregunta=p_capital_18)
db.session.add(p_capital_18)
db.session.add(r_capital_18)



# APLICAR CAMBIOS:
db.session.commit()

# MOSTRAR TABLAS:
print(Categoria.query.all())
print(Pregunta.query.all())
print(Respuesta.query.all())