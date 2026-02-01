from os import abort
import sys
from flask import redirect, render_template, request, session

from database import db
from service.Service import Service

def index():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  services = Service.query.all()
  return render_template('service/index.html', services=services, message=message)

def create():
  return render_template('service/create.html')

def store():
  name = request.form['name']
  description = request.form['description']
  price = request.form['price']
  
  service =  Service(
    name = name, 
    description = description, 
    price = price
  )
  
  db.session.add(service)
  db.session.commit()
  
  session['message'] = 'Layanan berhasil ditambah'
  
  return redirect('/service')

def edit(id):
  service = Service.query.filter_by(id=id).first()
  
  return render_template('service/edit.html', service=service)

def update(id):
  service = Service.query.filter_by(id=id).first()
  
  if service:
    service.name = request.form['name']
    service.description = request.form['description']
    service.price = request.form['price']
    db.session.commit()
    
    session['message'] = 'Layanan berhasil diubah'
    
    return redirect('/service')
    
  abort(404)
  
def destroy(id):
  service = Service.query.filter_by(id=id).first()
  
  if service:
    db.session.delete(service)
    db.session.commit()
    
    session['message'] = 'Layanan berhasil dihapus'
    
    return redirect('/service')
  
  abort(404)