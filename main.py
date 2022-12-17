import logging
import warnings
import hydra
import dotenv

from omegaconf import DictConfig
from src.flask_app import create_app, register_extensions

dotenv.load_dotenv()

log = logging.getLogger(__name__)


@hydra.main(config_path="configs", config_name="start_web_app")
def main(config: DictConfig):
    # Imports should be nested inside @hydra.main to optimize tab completion
    # Read more here: https://github.com/facebookresearch/hydra/issues/934

    app = create_app()

    register_extensions(app)

    if config.get("print_config"):
        from src.utils import print_config

        print_config(config, fields=tuple(config.keys()), resolve=True)

    if config.get("ignore_warnings"):
        log.info("Disabling python warnings! <config.ignore_warnings=True>")
        warnings.filterwarnings("ignore")

    if config.name == "start_web_app":
        from src import start_web_app
        return start_web_app(app, config)


if __name__ == '__main__':
    main()
