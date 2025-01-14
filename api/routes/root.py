from fastapi import APIRouter, Request, UploadFile, File, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from helpers.logger import logger
from controllers.cv_controller import process_cv

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse, tags=["essential"])
async def upload_screen(request: Request):
    logger.info("Serving the upload screen")
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...), consent: str = Form("new")):
    return await process_cv(file, consent)