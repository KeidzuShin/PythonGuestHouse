from database import db

class Room(db.Model):
  __tablename__ = 'room'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(32))
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  
  def __init__(self, name):
    self.name = name
    
  def __repr__(self) -> str:
    return f"{self.id}"