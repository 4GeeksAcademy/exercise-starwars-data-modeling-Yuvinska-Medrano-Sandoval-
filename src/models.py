import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#                NOTAS A TOMAR EN CUENTA 
# IMPORTANTE que cada class(una tabla) SIEMPRE lleve una llave primaria (PK)
# el nombre de la tabla siempre en minuscula 
# nullable = True ( se acepta que pase ) 
# nullable = False (es obligatorio que ponga algo ) 
# para crear una relacion necesitamos dos lineas 
#  / la primera se pone el nombre de la  tabla.el nombre de la linea 
#  /y la segunda se encarga de llamar a la tabla nombrada 
# String = Varchar 
# float se usa con numeros descimales , como el peso , la altura
# tener cuidado a la hora de escribir el codigo , tiene un orden, arriba hacia abajo 
# asegurate de que lo que quieras llamar esta escrito primero para despues poder llamarlo
# usuario ,personajes, planeta, nave de star wars.




class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    surname = Column(String(40), nullable = True)
    email = Column(String(50), unique = False)
    password = Column(String(30), nullable = False)
    


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    height = Column(Float, nullable = False)
    weight = Column(Float, nullable = True)
    hair_color = Column(String(15), nullable = True)
    skin_color = Column(String(15), nullable = True)


class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_idRelationship = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character_idRelationship = relationship(Character)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    weather = Column(String(100), nullable = True)
    land = Column(String(150), nullable = True)
    community = Column(String(250), nullable = True)
    
class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_idRelationship = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet_idRelationship = relationship(Planet)


class Star_Wars_Ship(Base):
    __tablename__ = 'star_wars_ship'
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    model = Column(String(50), nullable = False)
    material = Column(String(70), nullable = True)
    capacity = Column(String(30), nullable = True)


class Favorite_StarWarsShip(Base):
    __tablename__ = 'favorite_starwarsship'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_idRelationship = relationship(User)
    star_wars_ship_id = Column(Integer, ForeignKey('star_wars_ship.id'))
    star_wars_ship_idRelationship = relationship(Star_Wars_Ship)


    




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
