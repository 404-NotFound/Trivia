#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.trivia import db, Categorias

#CREO TABLAS
db.drop_all()
db.create_all()

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

# APLICAR CAMBIOS:
db.session.commit()


print(Categorias.query.all())