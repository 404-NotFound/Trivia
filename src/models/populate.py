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
r_capital_1 = Respuesta(text="Asunción", es_correcta=True, pregunta=p_capital_1)
r_capital_1_2 = Respuesta(text="Concepción", es_correcta=False, pregunta=p_capital_1)
r_capital_1_3 = Respuesta(text="Encarnación", es_correcta=False, pregunta=p_capital_1)
db.session.add(p_capital_1)
db.session.add(r_capital_1)

p_capital_2 = Pregunta(text='Cuál es la capital de Argentina', categoria=c_geografia)
r_capital_2 = Respuesta(text="Buenos Aires", es_correcta=True, pregunta=p_capital_2)
r_capital_2_2 = Respuesta(text="Capital Federal", es_correcta=True, pregunta=p_capital_2)
r_capital_2_3 = Respuesta(text="Gran Buenos Aires", es_correcta=False, pregunta=p_capital_2)
db.session.add(p_capital_2)
db.session.add(r_capital_2)

p_capital_3 = Pregunta(text='Cuál es la capital de Chile', categoria=c_geografia)
r_capital_3 = Respuesta(text="Santiago de Chile", es_correcta=True, pregunta=p_capital_3)
r_capital_3_2 = Respuesta(text="Santiago del Estero", es_correcta=False, pregunta=p_capital_3)
r_capital_3_3 = Respuesta(text="Valparaíso", es_correcta=False, pregunta=p_capital_3)
db.session.add(p_capital_3)
db.session.add(r_capital_3)

p_capital_4 = Pregunta(text='Cuál es la capital de Brasil', categoria=c_geografia)
r_capital_4 = Respuesta(text="Brasilia", es_correcta=True, pregunta=p_capital_4)
r_capital_4_2 = Respuesta(text="Porto Alegre", es_correcta=False, pregunta=p_capital_4)
r_capital_4_3 = Respuesta(text="Rìo de Janeirp", es_correcta=False, pregunta=p_capital_4)
db.session.add(p_capital_4)
db.session.add(r_capital_4)

p_capital_5 = Pregunta(text='Cuál es la capital de Venezuela', categoria=c_geografia)
r_capital_5 = Respuesta(text="Caracas", es_correcta=True, pregunta=p_capital_5)
r_capital_5_2 = Respuesta(text="Maracaibo", es_correcta=False, pregunta=p_capital_5)
r_capital_5_3 = Respuesta(text="Venezuela", es_correcta=False, pregunta=p_capital_5)
db.session.add(p_capital_5)
db.session.add(r_capital_5)

p_capital_6 = Pregunta(text='Cuál es la capital de Bolivia', categoria=c_geografia)
r_capital_6 = Respuesta(text="La Paz", es_correcta=True, pregunta=p_capital_6)
r_capital_6 = Respuesta(text="Santa Cruz de la Sierra", es_correcta=False, pregunta=p_capital_6)
r_capital_6_3 = Respuesta(text="Bolivia", es_correcta=False, pregunta=p_capital_6)
db.session.add(p_capital_6)
db.session.add(r_capital_6)

p_capital_7 = Pregunta(text='Cuál es la capital de Uruguay', categoria=c_geografia)
r_capital_7 = Respuesta(text="Montevideo", es_correcta=True, pregunta=p_capital_7)
r_capital_7 = Respuesta(text="Punta del Este", es_correcta=False, pregunta=p_capital_7)
r_capital_7 = Respuesta(text="Maldonado", es_correcta=False, pregunta=p_capital_7)
db.session.add(p_capital_7)
db.session.add(r_capital_7)

p_capital_8 = Pregunta(text='Cuál es la capital de Peru', categoria=c_geografia)
r_capital_8 = Respuesta(text="Lima", es_correcta=True, pregunta=p_capital_8)
r_capital_8 = Respuesta(text="Cusco", es_correcta=False, pregunta=p_capital_8)
r_capital_8 = Respuesta(text="Ica", es_correcta=False, pregunta=p_capital_8)
db.session.add(p_capital_8)
db.session.add(r_capital_8)

p_capital_9 = Pregunta(text='Cuál es la capital de Colombia', categoria=c_geografia)
r_capital_9 = Respuesta(text="Bogotá", es_correcta=True, pregunta=p_capital_9)
r_capital_9 = Respuesta(text="Medellín", es_correcta=False, pregunta=p_capital_9)
r_capital_9 = Respuesta(text="Colombia", es_correcta=False, pregunta=p_capital_9)
db.session.add(p_capital_9)
db.session.add(r_capital_9)

p_capital_10 = Pregunta(text='Cuál es la capital de Ecuador', categoria=c_geografia)
r_capital_10 = Respuesta(text="Quito", es_correcta=True, pregunta=p_capital_10)
r_capital_10_2 = Respuesta(text="Ecuador", es_correcta=False, pregunta=p_capital_10)
r_capital_10 = Respuesta(text="Guayaquil", es_correcta=False, pregunta=p_capital_10)
db.session.add(p_capital_10)
db.session.add(r_capital_10)

p_capital_11 = Pregunta(text='Cuál es la capital de México', categoria=c_geografia)
r_capital_11 = Respuesta(text="Ciudad de México", es_correcta=True, pregunta=p_capital_11)
r_capital_11_2 = Respuesta(text="México", es_correcta=False, pregunta=p_capital_11)
r_capital_11_3 = Respuesta(text="Guadalajara", es_correcta=False, pregunta=p_capital_11)
db.session.add(p_capital_11)
db.session.add(r_capital_11)

p_capital_12 = Pregunta(text='Cuál es la capital de Cuba', categoria=c_geografia)
r_capital_12 = Respuesta(text="La Habana", es_correcta=True, pregunta=p_capital_12)
r_capital_12_2 = Respuesta(text="La Habanera", es_correcta=False, pregunta=p_capital_12)
r_capital_12_3 = Respuesta(text="Santa Clara", es_correcta=False, pregunta=p_capital_12)
db.session.add(p_capital_12)
db.session.add(r_capital_12)

p_capital_13 = Pregunta(text='Cuál es la capital de Panamá', categoria=c_geografia)
r_capital_13 = Respuesta(text="Panamá", es_correcta=True, pregunta=p_capital_13)
r_capital_13_2 = Respuesta(text="Santiago", es_correcta=False, pregunta=p_capital_13)
r_capital_13_3 = Respuesta(text="Chimán", es_correcta=False, pregunta=p_capital_13)
db.session.add(p_capital_13)
db.session.add(r_capital_13)

p_capital_14 = Pregunta(text='Cuál es la capital de Portugal', categoria=c_geografia)
r_capital_14 = Respuesta(text="Lisboa", es_correcta=True, pregunta=p_capital_14)
r_capital_14_2 = Respuesta(text="Portuagal", es_correcta=False, pregunta=p_capital_14)
r_capital_14_3 = Respuesta(text="Oporto", es_correcta=False, pregunta=p_capital_14)
db.session.add(p_capital_14)
db.session.add(r_capital_14)

p_capital_15 = Pregunta(text='Cuál es la capital de España', categoria=c_geografia)
r_capital_15 = Respuesta(text="Madrid", es_correcta=True, pregunta=p_capital_15)
r_capital_15_2 = Respuesta(text="Barcelona", es_correcta=False, pregunta=p_capital_15)
r_capital_15_3 = Respuesta(text="Bilbao", es_correcta=False, pregunta=p_capital_15)
db.session.add(p_capital_15)
db.session.add(r_capital_15)

p_capital_16 = Pregunta(text='Cuál es la capital de Francia', categoria=c_geografia)
r_capital_16 = Respuesta(text="París", es_correcta=True, pregunta=p_capital_16)
r_capital_16_2 = Respuesta(text="Marsella", es_correcta=False, pregunta=p_capital_16)
r_capital_16_3 = Respuesta(text="Francia", es_correcta=False, pregunta=p_capital_16)
db.session.add(p_capital_16)
db.session.add(r_capital_16)

p_capital_17 = Pregunta(text='Cuál es la capital de República Dominicana', categoria=c_geografia)
r_capital_17 = Respuesta(text="Santo Domingo", es_correcta=True, pregunta=p_capital_17)
r_capital_17_2 = Respuesta(text="San Juan", es_correcta=False, pregunta=p_capital_17)
r_capital_17_3 = Respuesta(text="Puerto Rico", es_correcta=False, pregunta=p_capital_17)
db.session.add(p_capital_17)
db.session.add(r_capital_17)

p_capital_18 = Pregunta(text='Cuál es la capital de Italia', categoria=c_geografia)
r_capital_18 = Respuesta(text="Roma", es_correcta=True, pregunta=p_capital_18)
r_capital_18_2 = Respuesta(text="Grecia", es_correcta=False, pregunta=p_capital_18)
r_capital_18_3 = Respuesta(text="Atenas", es_correcta=False, pregunta=p_capital_18)
db.session.add(p_capital_18)
db.session.add(r_capital_18)



# APLICAR CAMBIOS:
db.session.commit()

# MOSTRAR TABLAS:
print(Categoria.query.all())
print(Pregunta.query.all())
print(Respuesta.query.all())