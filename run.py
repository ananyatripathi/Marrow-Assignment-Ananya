from app import create_app

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        from app import db  # Import db to create the tables
        db.create_all()  # Create tables if they do not exist
    app.run(debug=True)
