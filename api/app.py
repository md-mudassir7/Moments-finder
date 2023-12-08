from api.routers import shorts
from fastapi import FastAPI

def main_app():
    app = FastAPI()

    app.include_router(shorts.router)

    return app