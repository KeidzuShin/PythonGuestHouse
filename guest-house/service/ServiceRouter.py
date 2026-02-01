from flask import Blueprint

from service.ServiceController import destroy, edit, index, create, store, update

serviceRouter = Blueprint('service_bp', __name__)

serviceRouter.route('/', methods = ['GET']) (index)

serviceRouter.route('/create', methods = ['GET']) (create)

serviceRouter.route('/store', methods = ['POST']) (store)

serviceRouter.route('/<int:id>/edit', methods = ['GET']) (edit)

serviceRouter.route('/<int:id>/update', methods = ['POST']) (update)

serviceRouter.route('/<int:id>/destroy', methods = ['GET']) (destroy)