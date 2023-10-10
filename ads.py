from flask import Blueprint,jsonify, request
from sqlalchemy.sql import text
from db import db
import datetime

ads_blueprint = Blueprint('ads_blueprint',__name__)

@ads_blueprint.route('/ad-clicks')
def adClicks():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('SELECT * FROM ads WHERE date = "'+currentDate+'"')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()

    #check if its first click for the day or not
    rawdatalength = len(rawdata)

    # if fisrt click 
    if rawdatalength == 0:
        sqlins = text('INSERT INTO ads (date,clicks) VALUES ("'+currentDate+'",1)')
        db.engine.execute(sqlins)
    else:
        # fetch the old count 
        newclickvalue = rawdata[0].clicks + 1

        sqlupd = text('UPDATE ads SET clicks = '+str(newclickvalue)+' WHERE date = "'+currentDate+'"')
        db.engine.execute(sqlupd)
    
    return "Ad Click was logged"