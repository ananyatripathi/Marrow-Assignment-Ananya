from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize the database and migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register routes
    from .routes import register_routes
    register_routes(app)

    return app
