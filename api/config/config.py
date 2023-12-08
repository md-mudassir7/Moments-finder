#!/usr/bin/python3
# coding= utf-8
""" config file """
import base64
import json
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """ This class defines settings """
    
    # Uvicorn Server details
    uvicorn_host: str = "127.0.0.1"
    uvicorn_port: int = 8000

    # DB variables
    mongo_host: str = "localhost"
    mongo_port: str = "27017"
    mongo_username: str = ""
    mongo_password: str = ""
    mongo_auth_source: str = "admin"
    mongo_auth_mechanism: str = "SCRAM-SHA-256"
    
    shorts: str = "shorts"
    
    openapi_key: str = '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'

    @classmethod
    def get_settings(cls):
        """ get setting """
        return Settings()