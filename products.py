from flask import Blueprint,jsonify
from sqlalchemy.sql import text
from db import db
import datetime

product_blueprint = Blueprint('product_blueprint',__name__)

@product_blueprint.route('/products')
def products():
    # Tracking Visitors 
    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('SELECT * FROM visitors WHERE date = "'+currentDate+'"')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()

    #check if its first click for the day or not
    rawdatalength = len(rawdata)

    # if fisrt click 
    if rawdatalength == 0:
        sqlins = text('INSERT INTO visitors (date,count) VALUES ("'+currentDate+'",1)')
        db.engine.execute(sqlins)
    else:
        # fetch the old count 
        newcountvalue = rawdata[0].count + 1

        sqlupd = text('UPDATE visitors SET count = '+str(newcountvalue)+' WHERE date = "'+currentDate+'"')
        db.engine.execute(sqlupd)
    # End Tracking Visitors


    #Display all Products
    sql = text("SELECT * FROM products")
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata
