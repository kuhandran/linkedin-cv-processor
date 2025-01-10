from fastapi import APIRouter, UploadFile, File
from modules.cv_extractor import extract_education, extract_experience, extract_skills

router = APIRouter()

@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    # Save the uploaded file
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    
    # Process the CV
    cv_data = process_cv(f"uploads/{file.filename}")
    
    return {"filename": file.filename, "cv_data": cv_data}

def process_cv(file_path: str):
    # Extract information from the CV
    education = extract_education(file_path)
    experience = extract_experience(file_path)
    skills = extract_skills(file_path)
    
    # Combine all extracted information into a JSON format
    cv_json = {
        "education": education,
        "experience": experience,
        "skills": skills
    }
    
    return cv_json

