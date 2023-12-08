import uvicorn
from api.config.config import Settings
from api.app import main_app
from utility.logger import get_logger

logging = get_logger(__name__)
settings = Settings.get_settings()

def main():
    """
    This function creates fastapi object,
    loads settings, adds api routers and certificate configuration
    """
    app = main_app()

    # Define a custom logging configuration for access logs
    uvicorn.run(app, host=settings.uvicorn_host, port=settings.uvicorn_port)


if __name__ == "__main__":
    main()