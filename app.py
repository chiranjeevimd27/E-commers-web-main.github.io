from distutils.log import debug
from http import server
from flask import Flask
from db import db
from flask_cors import CORS
from products import product_blueprint
from contact import contact_blueprint
from ads import ads_blueprint
from dashboard import dashboard_blueprint
from adminlogin import adminlogin_blueprint
app = Flask(__name__)
CORS(app)

# Db Config
username = 'root'
password = ''
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'
dbname = '/webapp'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

# Register blueprint
app.register_blueprint(product_blueprint)
app.register_blueprint(contact_blueprint)
app.register_blueprint(ads_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(adminlogin_blueprint)

@app.route('/first-route')
def firstFunction():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
    app.run()