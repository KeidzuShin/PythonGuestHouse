from os import abort
import sys
from flask import redirect, render_template, request, session

from database import db
from room.Room import Room

def index():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  rooms = Room.query.all()
  return render_template('room/index.html', rooms=rooms, message=message)

def create():
  return render_template('room/create.html')

def store():
  name = request.form['name']
  
  room =  Room(name = name)
  
  db.session.add(room)
  db.session.commit()
  
  session['message'] = 'Kamar berhasil ditambah'
  
  return redirect('/room')

def edit(id):
  room = Room.query.filter_by(id=id).first()
  
  return render_template('room/edit.html', room=room)

def update(id):
  room = Room.query.filter_by(id=id).first()
  
  if room:
    room.name = request.form['name']
    db.session.commit()
    
    session['message'] = 'Kamar berhasil diubah'
    
    return redirect('/room')
    
  abort(404)
  
def destroy(id):
  room = Room.query.filter_by(id=id).first()
  
  if room:
    db.session.delete(room)
    db.session.commit()
    
    session['message'] = 'Kamar berhasil dihapus'
    
    return redirect('/room')
  
  abort(404)