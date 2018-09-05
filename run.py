from flask import Flask
from flask import request, jsonify
import sys
import logging
from database import *
import secrets, string

app = Flask(__name__)

@app.before_request
def before_request():
    init_db()

@app.before_request
def after_request():
    session.close()

@app.route('/', methods=['GET'])
def home():
    return "Hi"

@app.route('/register', methods=['POST'])
def register():
    user_name = request.form['user_name']
    user_email = request.form['user_email']
    alphabet = string.ascii_letters + string.digits
    gpassword = ''.join(secrets.choice(alphabet) for i in range(8))

    user = User(
        user_name = user_name,
        password = gpassword
        )

    session.add(user)
    session.flush()

    info = User_Info(
        user_id = user.id,
        user_email = user_email
        )

    session.add(info)
    try:
         session.commit()
         return "User Registered"
    except Exception as e:
       #log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
       session.rollback()
       session.flush() # for resetting non-commited .add()
       failed=True


if __name__ == '__main__':
    app.run(debug=True)
