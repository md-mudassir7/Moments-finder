#!/usr/bin/python3
# coding= utf-8
""" database module """


class DbConnection:
    """ dependency class for creating the DB connection """
    def __init__(self):
        from api.database.mongo.mongo_db import MongoDb
        self.db = MongoDb.get_db()


class DbCrud:
    """ abstract class for DB CRUD object """

    def get_transcription_by_title(self, db, name):
        pass

    @classmethod
    def get_db_crud(cls):
        """ This method returns MONGOCRUD object """
        from api.database.mongo.crud import MongoCrud
        return MongoCrud()