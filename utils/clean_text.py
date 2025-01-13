import re

def clean_text(text):
    # Remove unnecessary characters and fix spacing
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text