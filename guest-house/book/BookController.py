from os import abort
import sys
import pdfkit
from flask import redirect, render_template, request, session, make_response

from database import db
from book.Book import Book
from room.Room import Room
from guest.Guest import Guest
from service.Service import Service

def index():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  books = Book.query.all()
  return render_template('book/index.html', books=books, message=message)

def transaction():
  message = None
  if session.get('message'):
    message = session['message']
  session.pop('message', None)
  
  books = Book.query.all()
  return render_template('book/transaction.html', books=books, message=message)

def export():
  books = Book.query.all()
  html = render_template('book/export.html', books=books)
  wkhtml_path = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
  pdf = pdfkit.from_string(html, False, configuration = wkhtml_path)
  
  response = make_response(pdf)
  response.headers["Content-Type"] = "application/pdf"
  response.headers["Content-Disposition"] = "inline; filename=report.pdf"
  return response

def detail(id):  
  book = Book.query.filter_by(id=id).first()
  return render_template('book/detail.html', book=book)

def create():
  services = Service.query.all()
  rooms = Room.query.all()
  return render_template('book/create.html', services=services, rooms=rooms)

def store():
  identity_number = request.form['identity_number']
  name = request.form['name']
  email = request.form['email']
  address = request.form['address']
  phone_number = request.form['phone_number']
  room_id = request.form['room_id']
  from_date = request.form['from_date']
  to_date = request.form['to_date']
  service_id = request.form['service_id']
  
  service = Service.query.filter_by(id=service_id).first()
  
  if not service:
    abort(404)
  
  book =  Book(
    identity_number=identity_number,
    name = name,
    email = email,
    phone_number = phone_number,
    address = address,
    from_date = from_date,
    to_date = to_date,
    price = service.price,
    room_id = room_id,
    service_id = service_id,
    check_in = True
  )
  
  guest = Guest.query.filter_by(identity_number=identity_number).first()
  
  if not guest:
    guest = Guest(identity_number=identity_number, name=name, email=email, address=address, phone_number=phone_number)
    db.session.add(guest)
  
  db.session.add(book)
  db.session.commit()
  
  session['message'] = 'Pemesanan berhasil ditambah'
  
  return redirect('/book')