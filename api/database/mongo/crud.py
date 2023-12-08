
from api.config.config import Settings
from api.models.schemas import DbDocument
from api.database.database import DbCrud
settings = Settings.get_settings()


class MongoCrud(DbCrud):
    """ class MONGOCRUD """
    def __init__(self):
        super().__init__()

    def get_transcription_by_title(self, db, title):
        """
        This method returns documents based on title
        :param db: database connection
        :param title: get ingest based on title
        """
        collection = db['shorts']

        # Querying by title and returning a list of documents
        document = collection.find_one({"title": title})
        
        if document:
            return DbDocument.parse_obj(document)
        return None