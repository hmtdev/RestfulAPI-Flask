from flask import Flask, request, Blueprint
from .books.controller import books
from .extension import db
from dotenv import load_dotenv
from .models import Students, Books, Author, Category, Borrow
import os 



def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("Created all tables") 
    app.register_blueprint(books)
    return app
