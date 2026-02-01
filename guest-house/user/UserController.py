from audioop import add
from os import abort
import sys
from flask import redirect, render_template, request, session

from database import db
from user.User import User

def index():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  users = User.query.all()
  return render_template('user/index.html', users=users, message=message)

def create():
  return render_template('user/create.html')

def store():
  name = request.form['name']
  username = request.form['username']
  email = request.form['email']
  password = request.form['password']
  
  user = User(
    name = name, 
    email = email, 
    username = username,
    password = password
  )
  
  db.session.add(user)
  db.session.commit()
  
  session['message'] = 'User berhasil ditambah'
  
  return redirect('/user')

def edit(id):
  user = User.query.filter_by(id=id).first()
  
  return render_template('user/edit.html', user=user)

def update(id):
  user = User.query.filter_by(id=id).first()
  
  if user:
    user.name = request.form['name']
    user.username = request.form['username']
    user.email = request.form['email']
    user.password = request.form['password']
    db.session.commit()
    
    session['message'] = 'User berhasil diubah'
    
    return redirect('/user')
    
  abort(404)
  
def destroy(id):
  user = User.query.filter_by(id=id).first()
  
  if user:
    db.session.delete(user)
    db.session.commit()
    
    session['message'] = 'User berhasil dihapus'
    
    return redirect('/user')
  
  abort(404)