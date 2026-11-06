import re

def clean_text(text):
    """Normalize whitespace without destroying meaning or punctuation."""
    if not isinstance(text, str):
        return ''
    return re.sub(r'\s+', ' ', text).strip()
