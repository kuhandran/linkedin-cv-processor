from fastapi import APIRouter, HTTPException
from helpers.logger import logger
import json
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LANGUAGES_FILE = os.path.join(BASE_DIR, "..", "..", "data", "languages.json")

@router.get("/languages")
async def get_languages():
    try:
        with open(LANGUAGES_FILE, "r", encoding="utf-8") as f:
            languages_data = json.load(f)
        return languages_data
    except Exception as e:
        logger.error(f"Error in get_languages: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")