import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DefaultConfig')

if 'YOURAPPLICATION_SETTINGS' in os.environ:
    YOURAPPLICATION_SETTINGS = os.getenv('YOURAPPLICATION_SETTINGS')
    app.config.from_object(YOURAPPLICATION_SETTINGS)

db = SQLAlchemy(app)

from product_management.routes import product_management_bp
app.register_blueprint(product_management_bp)

from authentication.routes import authentication_bp
app.register_blueprint(authentication_bp)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
