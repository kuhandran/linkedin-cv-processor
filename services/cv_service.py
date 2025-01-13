from io import BytesIO
from helpers.cv_processor_helper import process_cv_with_debug
from utils.clean_text import clean_text
from models.profile_model import save_profile_to_db, get_profile_from_db, delete_all_profiles, get_profile_by_mobile
from helpers.logger import logger
from transformers import pipeline

async def process_cv_file(file, consent):
    if file.filename == "":
        raise ValueError("No file selected")

    pdf_file = BytesIO(file.file.read())
    resume_data = process_cv_with_debug(pdf_file)
    mobile_number = resume_data.get("Contact", {}).get("Phone", "")

    if not mobile_number:
        raise ValueError("Mobile number could not be extracted from the CV.")

    existing_profile = get_profile_by_mobile(mobile_number)

    if existing_profile and consent != "overwrite":
        raise ValueError(f"Mobile number {mobile_number} already exists. Click to overwrite.")

    profile_id = existing_profile.get("client_id", "generated_id") if existing_profile else "generated_id"

    # Save the extracted resume data
    profile_saved = save_profile_to_db(profile_id, resume_data)
    if not profile_saved:
        raise ValueError("Failed to save profile to database.")

    return {
        "message": "CV processed and profile saved successfully.",
        "resume_data": resume_data
    }

async def ask_question(client_id, question):
    profile = get_profile_from_db(client_id)
    if not profile:
        raise ValueError(f"No profile found for client_id: {client_id}")

    answer = generate_answer(profile, question)
    return {"answer": answer}

def generate_answer(profile: dict, question: str) -> str:
    try:
        model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
        context = clean_text(profile.get('summary', 'No summary available'))
        result = model(question=question, context=context)
        return result['answer']
    except Exception as e:
        logger.error(f"Error in generate_answer: {str(e)}")
        raise e

async def delete_profiles():
    try:
        deleted_count = delete_all_profiles()
        return {"message": f"Successfully deleted {deleted_count} profiles."}
    except Exception as e:
        logger.error(f"Error in delete_profiles: {str(e)}")
        raise e