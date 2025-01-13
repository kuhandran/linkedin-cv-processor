from fastapi import APIRouter, HTTPException
from helpers.logger import logger
from controllers.cv_controller import delete_profiles

router = APIRouter()

@router.delete("/delete_profiles")
async def delete_profiles_endpoint():
    try:
        return await delete_profiles()
    except Exception as e:
        logger.error(f"Error in delete_profiles: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")