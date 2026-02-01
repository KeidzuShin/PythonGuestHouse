from audioop import add
from os import abort
import sys
from flask import redirect, render_template, request, session

from database import db
from guest.Guest import Guest

def index():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  guests = Guest.query.all()
  return render_template('guest/index.html', guests=guests, message=message)

def create():
  return render_template('guest/create.html')

def store():
  name = request.form['name']
  email = request.form['email']
  address = request.form['address']
  phone_number = request.form['phone_number']
  identity_number = request.form['identity_number']
  
  guest = Guest(
    name = name, 
    email = email, 
    address = address, 
    phone_number = phone_number,
    identity_number = identity_number
  )
  
  db.session.add(guest)
  db.session.commit()
  
  session['message'] = 'Tamu berhasil ditambah'
  
  return redirect('/guest')

def edit(id):
  guest = Guest.query.filter_by(id=id).first()
  
  return render_template('guest/edit.html', guest=guest)

def update(id):
  guest = Guest.query.filter_by(id=id).first()
  
  if guest:
    guest.name = request.form['name']
    guest.email = request.form['email']
    guest.address = request.form['address']
    guest.phone_number = request.form['phone_number']
    guest.identity_number = request.form['identity_number']
    db.session.commit()
    
    session['message'] = 'Tamu berhasil diubah'
    
    return redirect('/guest')
    
  abort(404)
  
def destroy(id):
  guest = Guest.query.filter_by(id=id).first()
  
  if guest:
    db.session.delete(guest)
    db.session.commit()
    
    session['message'] = 'Tamu berhasil dihapus'
    
    return redirect('/guest')
  
  abort(404)