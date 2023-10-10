from flask import Blueprint,jsonify,request
from sqlalchemy.sql import text
from db import db
import datetime

adminlogin_blueprint = Blueprint('adminlogin_blueprint',__name__)

@adminlogin_blueprint.route('/admin-login',methods=['POST'])
def adminLogin():
    email = request.form['email']
    password = request.form['password']

    sql = text('SELECT * FROM users WHERE email = "'+email+'" And password = "'+password+'"')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    rawdatalength = len(rawdata)

    if rawdatalength == 0:
        return "0"
    else:
        return "1"