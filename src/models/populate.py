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

p1 = Pregunta(text='Cuál es la capital de Paraguay', categoria=c_geografia)
r1 = Respuesta(text="Asunción", pregunta=p1)
db.session.add(p1)
db.session.add(r1)

p2 = Pregunta(text='Cuál es la capital de Argentina', categoria=c_geografia)
r2 = Respuesta(text="Buenos Aires", pregunta=p2)
db.session.add(p2)
db.session.add(r2)

p3 = Pregunta(text='Cuál es la capital de Chile', categoria=c_geografia)
r3 = Respuesta(text="Santiago de Chile", pregunta=p3)
db.session.add(p3)
db.session.add(r3)

p4 = Pregunta(text='Cuál es la capital de Brasil', categoria=c_geografia)
r4 = Respuesta(text="Brasilia", pregunta=p4)
db.session.add(p4)
db.session.add(r4)

p5 = Pregunta(text='Cuál es la capital de Venezuela', categoria=c_geografia)
r5 = Respuesta(text="Caracas", pregunta=p5)
db.session.add(p5)
db.session.add(r5)

p6 = Pregunta(text='Cuál es la capital de Bolivia', categoria=c_geografia)
r6 = Respuesta(text="La Paz", pregunta=p6)
db.session.add(p6)
db.session.add(r6)

p7 = Pregunta(text='Cuál es la capital de Uruguay', categoria=c_geografia)
r7 = Respuesta(text="Montevideo", pregunta=p7)
db.session.add(p7)
db.session.add(r7)

p8 = Pregunta(text='Cuál es la capital de Peru', categoria=c_geografia)
r8 = Respuesta(text="Lima", pregunta=p8)
db.session.add(p8)
db.session.add(r8)

p9 = Pregunta(text='Cuál es la capital de Colombia', categoria=c_geografia)
r9 = Respuesta(text="Bogotá", pregunta=p9)
db.session.add(p9)
db.session.add(r9)

p10 = Pregunta(text='Cuál es la capital de Ecuador', categoria=c_geografia)
r10 = Respuesta(text="Quito", pregunta=p10)
db.session.add(p10)
db.session.add(r10)

p11 = Pregunta(text='Cuál es la capital de México', categoria=c_geografia)
r11 = Respuesta(text="México", pregunta=p11)
db.session.add(p11)
db.session.add(r11)

p12 = Pregunta(text='Cuál es la capital de Cuba', categoria=c_geografia)
r12 = Respuesta(text="La Habana", pregunta=p12)
db.session.add(p12)
db.session.add(r12)

p13 = Pregunta(text='Cuál es la capital de Panamá', categoria=c_geografia)
r13 = Respuesta(text="Panamá", pregunta=p13)
db.session.add(p13)
db.session.add(r13)

p14 = Pregunta(text='Cuál es la capital de Portugal', categoria=c_geografia)
r14 = Respuesta(text="Lisboa", pregunta=p14)
db.session.add(p14)
db.session.add(r14)

p15 = Pregunta(text='Cuál es la capital de España', categoria=c_geografia)
r15 = Respuesta(text="Madrid", pregunta=p15)
db.session.add(p15)
db.session.add(r15)

p16 = Pregunta(text='Cuál es la capital de Francia', categoria=c_geografia)
r16 = Respuesta(text="París", pregunta=p16)
db.session.add(p16)
db.session.add(r16)

p17 = Pregunta(text='Cuál es la capital de República Dominicana', categoria=c_geografia)
r17 = Respuesta(text="Santo Domingo", pregunta=p17)
db.session.add(p17)
db.session.add(r17)

p18 = Pregunta(text='Cuál es la capital de Italia', categoria=c_geografia)
r18 = Respuesta(text="Roma", pregunta=p18)
db.session.add(p18)
db.session.add(r18)

# APLICAR CAMBIOS:
db.session.commit()

print(Categoria.query.all())
print(Pregunta.query.all())
print(Respuesta.query.all())