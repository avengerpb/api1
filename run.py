from flask import Flask
from flask import request, jsonify
import sys
import logging
from database import *

app = Flask(__name__)



@app.before_request
def before_request():
    init_db()

@app.before_request
def after_request():
    session.close()

@app.route('/', methods=['GET'])
def home():
    user = User(
        user_name = 'Dat Le'
        )
    session.add(user)
    try:
         session.commit()
         return " OK Fine"
    except Exception as e:
       #log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
       session.rollback()
       session.flush() # for resetting non-commited .add()
       failed=True


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
