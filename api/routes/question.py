from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from helpers.logger import logger
from controllers.cv_controller import ask_question

router = APIRouter()

class QuestionRequest(BaseModel):
    client_id: str
    question: str

@router.post("/ask_question")
async def ask_question_endpoint(request: QuestionRequest):
    try:
        return await ask_question(request.client_id, request.question)
    except Exception as e:
        logger.error(f"Error in ask_question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the question: {str(e)}")