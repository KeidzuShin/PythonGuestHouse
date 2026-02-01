from database import db

class Service(db.Model):
  __tablename__ = 'services'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(32))
  description = db.Column(db.String(32))
  price = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self
  
  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price
    
  def __repr__(self) -> str:
    return f"{self.id}"