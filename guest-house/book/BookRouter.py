import sys
from flask import Blueprint

from book.BookController import detail, index, store, create, transaction, export

bookRouter = Blueprint('book_bp', __name__)

bookRouter.route('/', methods = ['GET']) (index)

bookRouter.route('/create', methods = ['GET']) (create)

bookRouter.route('/transaction', methods = ['GET']) (transaction)

bookRouter.route('/export', methods = ['GET']) (export)

bookRouter.route('/<int:id>', methods = ['GET']) (detail)

bookRouter.route('/store', methods = ['POST']) (store)