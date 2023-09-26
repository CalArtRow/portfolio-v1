from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '<ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAh0+dIz8p4P/YiwdV+VTCNrpkmP9OrUnYzQ7e3if7wYHAQr3FQtRWTfzBxqYauyJbiNX2TtKhweCifepDMd0g5orjrDiQ6X44+x7A+5Y/CddfxUqBTw6Vk5+F7Ampc89RNAlrV0NVE6GQjxyED67ImddTaktGg2GxZkYJuIEc2JbIbpYxu5zXa2ZqHO6JbXBdZbBLZ+5fzXlggJgRMOflhsUzsDyq7dMlhHaN2E4y83Fm4SR8gIV2NBFGX70Ce9Daxv/96e+hhwPpH2spvY9xDSGM2AvlXtmIxQ8sJr5ibgenEc+paVgF7P41wn1E50MzGNWZ5IHwf+k5FRHPhDUMnkND9eSKl14YZE/VU7WSpUtW70w3ln6IxI32oozRGcwhqICANdwYxQAZoBiMDp0xP8XZWA6Aiv5oOi0bWpqFQku7gpASkV/RGXBnAoBykW+n/rZjxzYXrjBUj5jLFD++/QZI+3cpCIm6LijH0J0tEF6FjSYRZBWBQunlHupBUj0= ID+c22100764@DSAF09E4AE597CD>'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22100764:DimByd2022!@csmysql.cs.cf.ac.uk:3306/c22100764_portfolio_db'




db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from portfolio import routes
