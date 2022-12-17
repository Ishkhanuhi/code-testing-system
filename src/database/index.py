from src.flask_app import create_app, register_extensions
app = create_app()

register_extensions(app)
