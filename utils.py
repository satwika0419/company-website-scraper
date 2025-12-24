import re
from urllib.parse import urlparse

EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
PHONE_REGEX = r"\+?\d[\d\s\-()]{7,}"

def extract_emails(text):
    return list(set(re.findall(EMAIL_REGEX, text)))

def extract_phones(text):
    return list(set(re.findall(PHONE_REGEX, text)))

def clean_text(text):
    return " ".join(text.split())

def is_internal_link(base_url, link):
    return urlparse(base_url).netloc == urlparse(link).netloc
