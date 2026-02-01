from database import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32))
  name = db.Column(db.String(32))
  email = db.Column(db.String(32))
  password = db.Column(db.String(32))
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
  
  def create(self):
    db.session.add(self)
    db.session.commit()
    return self
  
  def __init__(self, username, name, email, password):
    self.name = name
    self.username = username
    self.name = name
    self.email = email
    self.password = password
    
  def __repr__(self) -> str:
    return f"{self.id}"