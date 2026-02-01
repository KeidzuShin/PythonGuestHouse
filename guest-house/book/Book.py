from database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Book(db.Model):
  __tablename__ = 'book'
  id = db.Column(db.Integer, primary_key=True)
  identity_number = db.Column(db.String(32))
  name = db.Column(db.String(32))
  email = db.Column(db.String(32))
  phone_number = db.Column(db.String(32))
  address = db.Column(db.String(32))
  from_date = db.Column(db.DateTime)
  to_date = db.Column(db.DateTime)
  service_id = db.Column(db.Integer, ForeignKey('services.id'))
  room_id = db.Column(db.Integer, ForeignKey('room.id'), server_default=None)
  price = db.Column(db.Integer, server_default=None)
  check_in = db.Column(db.Boolean, server_default=None)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  
  service = relationship('Service')
  room = relationship('Room')
  
  def __init__(self, identity_number, name, email, phone_number, address, from_date, to_date, service_id, room_id, price, check_in):
    self.identity_number = identity_number
    self.name = name
    self.email = email
    self.phone_number = phone_number
    self.address = address
    self.from_date = from_date
    self.to_date = to_date
    self.service_id = service_id
    self.room_id = room_id
    self.price = price
    self.check_in = check_in