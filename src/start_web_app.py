from omegaconf import DictConfig
from src.flask_app import register_blueprints
from src.flask_app.dash_app import register_dash_app


def start_web_app(app, config: DictConfig) -> None:
    # register_blueprints(app)
    register_dash_app(app, config)

    app.run(host=config.host, port=config.port, debug=config.debug)
