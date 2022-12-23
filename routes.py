from flask import Blueprint
from controllers import add_quote, get_quote, hello, get_doc

api = Blueprint('urls', __name__,)

api.route('/', methods=['GET'])(hello)
api.route('/add', methods=['POST'])(add_quote)
api.route('/quote', methods=['GET'])(get_quote)
api.route('/doc', methods=['GET'])(get_doc)
