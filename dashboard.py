from flask import Blueprint,jsonify, request
from sqlalchemy.sql import text
from db import db
import datetime

dashboard_blueprint = Blueprint('dashboard_blueprint',__name__)

@dashboard_blueprint.route('/today-visitors')
def todayVisitors():

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

    sql = text('SELECT * FROM visitors WHERE date = "'+currentDate+'"')
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/overall-visitors')
def overallVisitors():
    sql = text("SELECT SUM(count) AS total_visitors FROM visitors")
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata


@dashboard_blueprint.route('/total-ad-clicks')
def totalAdClicks():
    sql = text("SELECT SUM(clicks) AS total_clicks FROM ads")
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/contact-details')
def contactDetails():
    sql = text("SELECT * FROM contact_form")
    result = db.engine.execute(sql)
    rawdata = result.fetchall()
    jsondata = jsonify([dict(row) for row in rawdata])
    return jsondata

@dashboard_blueprint.route('/barchart')
def barchart():

    x = ''
    for m in range(1,13):
        sql = text('SELECT SUM(count) AS total_count FROM visitors WHERE Month(date) = "'+str(m)+'"')
        result = db.engine.execute(sql)
        rawdata = result.fetchall()
        totalvisitorsbymonth = rawdata[0].total_count    
        x+= '{"month":"'+str(totalvisitorsbymonth)+'"},'

    x = x[:-1]
    rawjson = '['+x+']'
    return rawjson
