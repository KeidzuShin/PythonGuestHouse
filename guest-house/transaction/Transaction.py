from select import select
from database import db

class Transaction(db.Model):
  __tablename__ = 'transaction'
  id = db.Column(db.Integer, primary_key=True)
  guest_id = db.Column(db.Integer)
  service_id = db.Column(db.Integer)
  room_id = db.Column(db.Integer)
  price = db.Column(db.Integer)
  from_date = db.Column(db.DateTime)
  to_date = db.Column(db.DateTime)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  
  def __init__(self, guest_id, service_id, price, from_date, to_date):
    self.guest_id = guest_id
    self.service_id = service_id
    self.price = price
    self.from_date = from_date
    self.to_date = to_date
    
  def __repr__(self) -> str:
    return f"{self.id}"