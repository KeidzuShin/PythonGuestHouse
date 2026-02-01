from flask import Blueprint

from guest.GuestController import destroy, edit, index, create, store, update

guestRouter = Blueprint('guest_bp', __name__)

guestRouter.route('/', methods = ['GET']) (index)

guestRouter.route('/create', methods = ['GET']) (create)

guestRouter.route('/store', methods = ['POST']) (store)

guestRouter.route('/<int:id>/edit', methods = ['GET']) (edit)

guestRouter.route('/<int:id>/update', methods = ['POST']) (update)

guestRouter.route('/<int:id>/destroy', methods = ['GET']) (destroy)