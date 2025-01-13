from fastapi import HTTPException
from services.cv_service import process_cv_file, ask_question, delete_profiles
from helpers.logger import logger

async def process_cv(file, consent):
    try:
        return await process_cv_file(file, consent)
    except ValueError as e:
        logger.error(f"Error in process_cv: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def ask_question_endpoint(client_id, question):
    try:
        return await ask_question(client_id, question)
    except ValueError as e:
        logger.error(f"Error in ask_question: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

async def delete_profiles_endpoint():
    try:
        return await delete_profiles()
    except Exception as e:
        logger.error(f"Error in delete_profiles: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))