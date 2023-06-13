from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'
    
    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    birthday = db.Column(db.String)
    
    animals = db.relationship('Animal', back_populates='zookeeper')

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    
    animals = db.relationship('Animal', back_populates='enclosure')

class Animal(db.Model):
    __tablename__ = 'animals'
    
    name = db.Column(db.String, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String)
    
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))
    enclosure_id  = db.Column(db.Integer, db.ForeignKey('enclosure.id'))
    
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosures = db.relationship('Enclousre', back_populates='animals')
    
    
    
