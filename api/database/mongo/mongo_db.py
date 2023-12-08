#!/usr/bin/python3
# coding= utf-8
""" mongodb """
import logging

from pymongo import MongoClient

from api.config.config import Settings
import os

class MongoDb:
    """ This class defines MongoDB settings """
    settings = Settings.get_settings()
    client = MongoClient(
        host=settings.mongo_host,
        port=int(settings.mongo_port),
        username=settings.mongo_username,
        password=settings.mongo_password,
    )
    db = client[settings.shorts]

    @classmethod
    def get_db(cls):
        """ get db """
        settings = Settings.get_settings()
        logging.debug(f"Returning DB instance host:{settings.mongo_host}")
        return MongoDb.db