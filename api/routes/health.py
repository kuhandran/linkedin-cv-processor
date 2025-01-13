from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from helpers.logger import logger

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/health", response_class=HTMLResponse)
async def health(request: Request):
    logger.info("Health check endpoint called")
    return templates.TemplateResponse("health.html", {"request": request})

@router.get("/api/health")
async def api_health():
    logger.info("Health check API endpoint called")
    return {"status": "healthy"}