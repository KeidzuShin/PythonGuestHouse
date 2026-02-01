from flask import Blueprint

from user.UserController import destroy, edit, index, create, store, update

userRouter = Blueprint('user_bp', __name__)

userRouter.route('/', methods = ['GET']) (index)

userRouter.route('/create', methods = ['GET']) (create)

userRouter.route('/store', methods = ['POST']) (store)

userRouter.route('/<int:id>/edit', methods = ['GET']) (edit)

userRouter.route('/<int:id>/update', methods = ['POST']) (update)

userRouter.route('/<int:id>/destroy', methods = ['GET']) (destroy)