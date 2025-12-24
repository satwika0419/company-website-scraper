import json
from datetime import datetime
from crawler import crawl_site
from extractor import extract_company_info

def run_scraper(url):
    pages, visited = crawl_site(url)
    data = extract_company_info(url, pages)

    data["metadata"] = {
        "scrape_timestamp": datetime.utcnow().isoformat(),
        "pages_visited": visited,
        "errors_or_limitations": []
    }

    return data

if __name__ == "__main__":
    url = input("Enter company website URL: ").strip()
    result = run_scraper(url)
    print(json.dumps(result, indent=2))
