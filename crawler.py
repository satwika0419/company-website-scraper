import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import is_internal_link

HEADERS = {"User-Agent": "Mozilla/5.0"}

PRIORITY_KEYWORDS = [
    "about", "company", "product", "solution",
    "industry", "pricing", "contact", "career"
]

def crawl_site(base_url, max_pages=12):
    visited = set()
    to_visit = [base_url]
    pages = {}

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            response = requests.get(url, headers=HEADERS, timeout=8)
            soup = BeautifulSoup(response.text, "html.parser")

            visited.add(url)
            pages[url] = soup.get_text(" ", strip=True)

            for link in soup.find_all("a", href=True):
                full_link = urljoin(base_url, link["href"])
                if is_internal_link(base_url, full_link):
                    if any(k in full_link.lower() for k in PRIORITY_KEYWORDS):
                        if full_link not in visited:
                            to_visit.append(full_link)

        except Exception:
            visited.add(url)

    return pages, list(visited)
