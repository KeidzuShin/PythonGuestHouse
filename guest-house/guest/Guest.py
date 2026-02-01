from database import db

class Guest(db.Model):
  __tablename__ = 'guest'
  id = db.Column(db.Integer, primary_key=True)
  identity_number = db.Column(db.String(32))
  name = db.Column(db.String(32))
  email = db.Column(db.String(32))
  address = db.Column(db.String(32))
  phone_number = db.Column(db.String(32))
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self
  
  def __init__(self, identity_number, name, email, address, phone_number) -> None:
    self.identity_number = identity_number
    self.name = name
    self.email = email
    self.address = address
    self.phone_number = phone_number
    
  def __repr__(self) -> str:
    return f"{self.id}"