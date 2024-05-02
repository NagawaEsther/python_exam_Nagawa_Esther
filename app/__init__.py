from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy db object
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)


    # Import blueprints
    from app.controllers.Products_controllers import products
    
    
    # Register blueprints
    app.register_blueprint(products, url_prefix='/api/v1/products')
    

    @app.route('/')
    def home():
        return "Hello world"


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
