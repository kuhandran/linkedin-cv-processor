import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

def extract_education(file_path: str):
    # Read the file content
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Process the text with spaCy
    doc = nlp(text)
    
    # Use spaCy's rule-based matching to find education information
    matcher = Matcher(nlp.vocab)
    education_pattern = [{"LOWER": {"IN": ["bachelor", "master", "phd", "doctorate"]}},
                         {"LOWER": "in"},
                         {"POS": "PROPN", "OP": "+"}]
    matcher.add("EDUCATION", [education_pattern])
    
    matches = matcher(doc)
    education = [doc[start:end].text for _, start, end in matches]
    
    return education

def extract_experience(file_path: str):
    # Placeholder function - in a real scenario, this would be more complex
    with open(file_path, 'r') as file:
        text = file.read()
    
    doc = nlp(text)
    
    # Simple extraction based on job titles (this is a very basic approach)
    job_titles = [ent.text for ent in doc.ents if ent.label_ == "WORK_OF_ART"]
    
    return job_titles

def extract_skills(file_path: str):
    # Placeholder function - in a real scenario, this would use a predefined list of skills
    with open(file_path, 'r') as file:
        text = file.read()
    
    doc = nlp(text)
    
    # Simple extraction based on noun chunks (this is a very basic approach)
    skills = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]
    
    return skills

