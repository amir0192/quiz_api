from flask import Flask
from database import db

app = Flask(__name__)
# настройка базы данных
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quize_api.db"
# регистрируем базу на проект (подключить sql к flask)
db.init_app(app)

