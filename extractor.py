from utils import extract_emails, extract_phones, clean_text

def extract_company_info(url, pages):
    combined_text = " ".join(pages.values())

    emails = extract_emails(combined_text)
    phones = extract_phones(combined_text)

    social_links = {}
    for platform in ["linkedin", "twitter", "instagram", "youtube"]:
        if platform in combined_text.lower():
            social_links[platform] = "found"

    return {
        "identity": {
            "company_name": url.replace("https://", "").replace("http://", "").split(".")[0].title(),
            "website": url,
            "tagline": "not found"
        },
        "business_summary": {
            "what_they_do": clean_text(combined_text[:400]),
            "primary_offerings": [],
            "target_customers": []
        },
        "evidence": {
            "key_pages_detected": list(pages.keys()),
            "signals": [],
            "social_links": social_links
        },
        "contact_and_location": {
            "emails": emails,
            "phones": phones,
            "address": "not found",
            "contact_page": next((p for p in pages if "contact" in p.lower()), "")
        },
        "team_and_hiring": {
            "careers_page": next((p for p in pages if "career" in p.lower()), ""),
            "roles_detected": []
        }
    }
