__Author__ = "Amir Mallaei"

from flask import Flask, request
from flask import jsonify
from datetime import timedelta
from dotenv import load_dotenv
from utils.db import db
from validate_email import validate_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import random
import smtplib
import ssl

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
load_dotenv()

# JWT Configuration
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=60)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=90)
jwt = JWTManager(app)


# TODO : Needs Throtteli ng to avoid spam
@app.route("/email", methods=['POST'])
def email_check():
    """Check if Email is valid and send OTP token to the Email Address"""
    try:
        email = request.json['email']
    except Exception:
        return jsonify({'message': "Incorrect Data"}), 400

    is_valid = validate_email(email)
    if not is_valid:  # Return bad request if Email is not Valid
        return jsonify({'message': 'Not a vali email!'}), 400
    try:
        token = str(random.randint(100000, 999999))
        db.insert_auth(email, token)  # TODO: Taking Care of multiple Login
    except Exception:
        token = "000000"

    send_email(email, token)
    return jsonify({'message': is_valid}), 200


# TODO: Needs Throtteling to avoid spam
@app.route("/login", methods=["POST"])
def login():
    """Check Email & Token and send Access and Refresh token if it is valid"""
    try:
        email = request.json['email']
        token = request.json['token']
    except Exception:
        return jsonify({'message': "Incorrect Data"}), 400

    if not email or not token or len(token) != 6:
        return jsonify({'message': "Incorrect Data"}), 400

    db_token = db.get_code(email)
    if not token == db_token:
        return jsonify({'message': "Incorrect Data"}), 400
    access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)
    db.insert_update_jwt(access_token, refresh_token, email)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    """ Refresh the Access Token if it is Expired"""
    email = get_jwt_identity()
    access_token = create_access_token(identity=email, fresh=False)
    refresh_token = create_refresh_token(identity=email)
    db.insert_update_jwt(access_token, refresh_token, email)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200


@app.route("/logout", methods=["POST"])
@jwt_required(refresh=True)
def logout():
    """Logout User and remove Token"""
    email = get_jwt_identity()
    token = str(random.randint(100000, 999999))
    db.insert_update_jwt(token, "", email)
    unset_jwt_cookies(response)
    return jsonify({"msg": "logout successful"}), 200


def send_email(email, token):
    """Send Email and Token to user to login"""
    msg = MIMEMultipart()
    html = f"""\
    <html>
      <body style="background-color: black;  padding-top: 10px ;
            padding-bottom: 10px ;">
          <center>
           <h1 style="color: white;">VERIFY CODE:</h1>
           <h1 style="color: white;">{token}</h1>
           <center/>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))
    Password = os.getenv('EMAIL_PASSWORD')
    msg['From'] = os.getenv('SENDER_EMAIL')
    msg['To'] = email
    msg['Subject'] = "Consult Project Token"
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], Password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    except Exception:
        pass
    server.quit()
    return server


if __name__ == '__main__':
    app.run(debug=True)
