import os
import json

from services.file_processing import extract_text_from_pdf
from services.extract_contact import extract_contact
# from app.modules.skill_extraction import extract_top_skills
# from app.modules.language_detection import extract_languages
# from app.modules.education_extraction import extract_education
# from app.modules.experience_extraction import extract_experience
# from app.modules.certifications_extraction import extract_certifications
# from app.modules.honors_awards_extraction import extract_honors_awards
# from app.modules.summary_extraction import extract_summary

def extract_with_error_handling(func, lines):
    try:
        return func(lines)
    except Exception as e:
        print(f"Error extracting {func.__name__}: {e}")
        return None  # or an appropriate default value

def process_cv_with_debug(pdf_file):
    lines = extract_text_from_pdf(pdf_file)

    print(f"Extracted {(lines)}")
    
    # resume_info = {
    #     "Contact": extract_with_error_handling(extract_contact, lines),
    #     "Top Skills": extract_with_error_handling(extract_top_skills, lines),
    #     "Languages": extract_with_error_handling(extract_languages, lines),
    #     "Certifications": extract_with_error_handling(extract_certifications, lines),  # Implement as needed
    #     "Honors-Awards": extract_with_error_handling(extract_honors_awards, lines),   # Implement as needed
    #     "Summary": extract_with_error_handling(extract_summary, lines),         # Implement as needed
    #     "Experience": extract_with_error_handling(extract_experience, lines),
    #     "Education": extract_with_error_handling(extract_education, lines),
    # }

    resume_info = {
        "Contact": extract_with_error_handling(extract_contact, lines),
        "Top Skills": [],
        "Languages": [],
        "Certifications": [], # Implement as needed
        "Honors-Awards": [],  # Implement as needed
        "Summary": [],     # Implement as needed
        "Experience": [],
        "Education": [],
    }

    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    file_path = os.path.join('uploads', 'resume_info.json')
    with open(file_path, 'w') as json_file:
        json.dump(resume_info, json_file, indent=4)

    print(f"Resume information saved to {file_path}")
    return resume_info