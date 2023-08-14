from flask_sqlalchemy import SQLAlchemy

# создаем объект к классу sql(создаем его для удобства в models)
db=SQLAlchemy()

# импорт всех функций из файлов для дб
from database.leaderservice import *
from database.questionservice import *
from database.registerservice import *
