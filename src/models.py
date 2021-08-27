import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=False, nullable=False)
    first_name = Column(String(120), unique= False, nullable=False)
    last_name = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=False, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    favorite_planets = relationship("Favorite", back_populates="planet")

    def to_dict(self):
        return {
        '<user %s>' % self.user
        }


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False)
    planet_id = Column(ForeignKey('planet.id'), nullable=True)
    character_id = Column(ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(ForeignKey('vehicle.id'), nullable=True)
    user = relationship("Planet", back_populates="users")
    planet = relationship("User", back_populates="favorite_planets")


    def to_dict(self):
        return {
        '<favorite %s>' % self.favorite
        }


    def serialize(self):
        return {
            "character_id": self.character_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id
        }

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False, nullable=False)
    height = Column(String(120), unique=False, nullable=False)
    hair_color = Column(String(120), unique=False, nullable=False)
    eye_color = Column(String(120), unique=False, nullable=False)
    birth_year = Column(String(120), unique=False, nullable=False)
    gender = Column(String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False, nullable=False)
    population = Column(Integer, unique=False, nullable=False)
    terrain = Column(String(120), unique=False, nullable=False)
    climate = Column(String(120), unique=False, nullable=False)
    diameter = Column(Integer, unique=False, nullable=False)
    gravity = Column(String(120), unique=False, nullable=False)
    users = relationship("Favorite", back_populates="user")

    def to_dict(self):
        return {
        '<planet %s>' % self.planet
        }


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "gravity": self.gravity,
            "climate": self.climate,
            "diameter": self.diameter
        }

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=False, nullable=False)
    model = Column(String(120), unique=False, nullable=False)
    manufaturer = Column(String(120), unique=False, nullable=False)
    cost_in_credits = Column(Integer, unique=False, nullable=False)
    cargo_capacity = Column(Integer, unique=False, nullable=False)
    vehicle_class = Column(String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<vehicle %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufaturer": self.manufaturer,
            "cost_in_credits": self.cost_in_credits,
            "cargo_capacity": self.cargo_capacity,
            "vehicle_class": self.vehicle_class
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')