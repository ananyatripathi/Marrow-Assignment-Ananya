from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate

db = SQLAlchemy()
migrate = Migrate()  # Create a Migrate instance
