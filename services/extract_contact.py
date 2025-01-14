import re
import spacy
from transformers import pipeline
import requests
nlp = spacy.load("en_core_web_sm")
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# OpenCage API details
API_KEY = 'a207c914ba174cb6b4524f9f1537aff2'
BASE_URL = 'https://api.opencagedata.com/geocode/v1/json'


def extract_contact(lines):
    contact_info = {
        "Name": "",
        "Phone": "",
        "Email": "",
        "Location": ""
    }

    print(f"Lines to process: {lines}")

    for line in lines:
        line = line.strip()

        # Extract Name
        if line.startswith("Contact"):
            contact_info["Name"] = line.split("Contact", 1)[1].strip()

        # Regex to match phone numbers with labels like Home, Mobile, etc.
        phone_match = re.search(r'(\+\d{7,})\s*\((\w+)\)', line)
        if phone_match:
            contact_info['Phone'] = phone_match.group(1).strip()
            contact_info['PhoneType'] = phone_match.group(2).strip()

        # Extract Email Address
        email_match = re.search(r'\S+@\S+', line)
        if email_match:
            contact_info["Email"] = email_match.group(0).strip()

    # Combine all lines for location extraction
    full_text = " ".join(lines)

    # Extract locations using SpaCy
    doc = nlp(full_text)
    locations_spacy = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    # Extract locations using Hugging Face Transformers
    ner_results = ner_pipeline(full_text)
    locations_transformers = [ent['word'] for ent in ner_results if ent['entity'] in ['B-LOC', 'I-LOC']]

    # Combine unique locations
    all_locations = set(locations_spacy + locations_transformers)

    # Filter and format location
    if all_locations:
        valid_locations = [loc for loc in all_locations if len(loc.split()) > 1]  # Example filter
        contact_info["Location"] = ", ".join(valid_locations).strip()

    # Get the current location
    current_location = get_current_location()

    # Match extracted location with current location
    if contact_info["Location"] and current_location:
        location_parts = contact_info["Location"].split(", ", 1)
        current_location_parts = current_location.split(", ", 1)

        if len(location_parts) == 2 and len(current_location_parts) == 2:
            city, country = location_parts
            current_city, current_country = current_location_parts

            if city.lower() == current_city.lower() or country.lower() == current_country.lower():
                contact_info["Location"] = f"{city}, {country}"
            else:
                contact_info["Location"] = ""
        else:
            contact_info["Location"] = ""
    else:
        contact_info["Location"] = ""

    # Get formatted address using OpenCage
    if contact_info["Location"]:
        formatted_address, city, country = get_address_from_opencage(contact_info["Location"])
        if formatted_address:
            contact_info["Location"] = formatted_address

    return contact_info


def get_address_from_opencage(location):
    params = {
        'q': location,
        'key': API_KEY,
        'pretty': 1,
        'no_annotations': 1
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            formatted_address = data['results'][0]['formatted']
            city = data['results'][0]['components'].get('city', '')
            country = data['results'][0]['components'].get('country', '')
            return formatted_address, city, country
    return None, None, None


def get_current_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        if response.status_code == 200:
            data = response.json()
            city = data.get('city', '')
            country = data.get('country', '')
            return f"{city}, {country}"
    except Exception as e:
        print(f"Error fetching current location: {e}")

    return None


