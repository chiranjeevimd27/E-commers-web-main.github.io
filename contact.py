from flask import Blueprint,jsonify, request
from sqlalchemy.sql import text
from db import db
import datetime

contact_blueprint = Blueprint('contact_blueprint',__name__)

@contact_blueprint.route('/contact-data',methods=['POST'])
def addContactData():
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    comments = request.form['comments']

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('INSERT INTO contact_form (name,email,mobile,comments,date) VALUES ("'+name+'","'+email+'","'+mobile+'","'+comments+'","'+currentDate+'")')
    db.engine.execute(sql)
    return "Thank You For Contacting Us"