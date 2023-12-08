from fastapi import APIRouter, Depends, HTTPException
from api.models import schemas
from api.database.database import DbConnection , DbCrud
from highlight_generator.prompter import Prompter
from utility.logger import get_logger
router = APIRouter(
    prefix="/api/v1/shorts",
    tags=["shorts"],
    responses={404: {"description": "Not found"}},
)

logger = get_logger(__name__)

@router.post("/")
async def process(req: schemas.RequestModel,conn=Depends(DbConnection)):
    
    logger.info(f"Recieved short detection for Title : {req.title} and Genre : {req.genre}")
    crud = DbCrud.get_db_crud()
    db_doc = crud.get_transcription_by_title(conn.db, title=req.title)
    if not db_doc:
        raise HTTPException(status_code=404, detail="Transcription not found for the given title")

    transcription = db_doc.transcription

    if transcription is None:
        raise HTTPException(status_code=404, detail="Transcription field is missing in the document")

    logger.info("Creating a prompt for chatgpt")
    
    prompt_inst = Prompter(genre=req.genre,transcription=transcription)
    
    prompt_resp = prompt_inst.create_chat()
    
    logger.info("Prompting Completed")
    
    if type(prompt_resp) not in [type(2.8),type(1)]:
        return {"prompt response":f"Based on the transcription provided, there is no specific timestamp that can be considered a {req.genre} scene"}

    return {"prompt response": f"{db_doc.url}&t={prompt_resp}s"}