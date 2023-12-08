from pydantic import BaseModel, Field

from api.models.pydantic_objectid import PyObjectId


class RequestModel(BaseModel):
    title: str
    genre: str


class ResponseModel(BaseModel):
    id: PyObjectId
    title: str


class DbDocument(BaseModel):
    _id: PyObjectId
    title: str
    transcription: str
    url: str