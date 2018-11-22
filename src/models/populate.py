#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.trivia import db, Categorias, Preguntas, Respuestas

#CREO TABLAS
db.drop_all()
db.create_all()

#===============================================#
#                   CATEGORIAS                  #
#===============================================#

#CREO OBJETOS
historia = Categorias(nombre='Historia')
arte = Categorias(nombre='Arte')
geografia = Categorias(nombre='Geografía')
deporte = Categorias(nombre='Deporte')

# AGREGAR A LA DB
db.session.add(historia)
db.session.add(arte)
db.session.add(geografia)
db.session.add(deporte)

db.session.commit()
#===============================================#
#           PREGUNTAS Y RESPUETAS               #
#===============================================#

p1 = Preguntas(text='Cuál es la capital de Paraguay')
r1 = Respuestas(text="Asunción")
db.session.add(p1)
db.session.add(r1)

p2 = Preguntas(text='Cuál es la capital de Argentina')
r2 = Respuestas(text="Buenos Aires")
db.session.add(p2)
db.session.add(r2)

p2 = Preguntas(text='Cuál es la capital de Chile')
r2 = Respuestas(text="Santiago de Chile")
db.session.add(p2)
db.session.add(r2)

p3 = Preguntas(text='Cuál es la capital de Brasil')
r3 = Respuestas(text="Brasilia")
db.session.add(p3)
db.session.add(r3)

p4 = Preguntas(text='Cuál es la capital de Venezuela')
r4 = Respuestas(text="Caracas")
db.session.add(p4)
db.session.add(r4)

p5 = Preguntas(text='Cuál es la capital de Bolivia')
r5 = Respuestas(text="La Paz")
db.session.add(p5)
db.session.add(r5)

p6 = Preguntas(text='Cuál es la capital de Uruguay')
r6 = Respuestas(text="Montevideo")
db.session.add(p6)
db.session.add(r6)

p7 = Preguntas(text='Cuál es la capital de Peru')
r7 = Respuestas(text="Lima")
db.session.add(p7)
db.session.add(r7)

p8 = Preguntas(text='Cuál es la capital de Colombia')
r8 = Respuestas(text="Bogotá")
db.session.add(p8)
db.session.add(r8)

p9 = Preguntas(text='Cuál es la capital de Ecuador')
r9 = Respuestas(text="Quito")
db.session.add(p9)
db.session.add(r9)

p10 = Preguntas(text='Cuál es la capital de México')
r10 = Respuestas(text="México")
db.session.add(p10)
db.session.add(r10)

p11 = Preguntas(text='Cuál es la capital de Cuba')
r11 = Respuestas(text="La Habana")
db.session.add(p11)
db.session.add(r11)

p12 = Preguntas(text='Cuál es la capital de Panamá')
r12 = Respuestas(text="Panamá")
db.session.add(p12)
db.session.add(r12)

p13 = Preguntas(text='Cuál es la capital de Portugal')
r13 = Respuestas(text="Lisboa")
db.session.add(p13)
db.session.add(r13)

p14 = Preguntas(text='Cuál es la capital de España')
r14 = Respuestas(text="Madrid")
db.session.add(p14)
db.session.add(r14)

p15 = Preguntas(text='Cuál es la capital de Francia')
r15 = Respuestas(text="París")
db.session.add(p15)
db.session.add(r15)

p16 = Preguntas(text='Cuál es la capital de República Dominicana')
r16 = Respuestas(text="Santo Domingo")
db.session.add(p16)
db.session.add(r16)

p17 = Preguntas(text='Cuál es la capital de Italia')
r17 = Respuestas(text="Roma")
db.session.add(p17)
db.session.add(r17)

# APLICAR CAMBIOS:
db.session.commit()

print(Categorias.query.all())
print(Preguntas.query.all())
print(Respuestas.query.all())