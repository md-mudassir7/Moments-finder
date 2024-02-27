from api.routers import analyze
from fastapi import FastAPI

def main_app():
    app = FastAPI()

    app.include_router(analyze.router)

    return app