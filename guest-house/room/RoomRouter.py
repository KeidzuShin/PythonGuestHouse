from flask import Blueprint

from room.RoomController import destroy, edit, index, create, store, update

roomRouter = Blueprint('room_bp', __name__)

roomRouter.route('/', methods = ['GET']) (index)

roomRouter.route('/create', methods = ['GET']) (create)

roomRouter.route('/store', methods = ['POST']) (store)

roomRouter.route('/<int:id>/edit', methods = ['GET']) (edit)

roomRouter.route('/<int:id>/update', methods = ['POST']) (update)

roomRouter.route('/<int:id>/destroy', methods = ['GET']) (destroy)