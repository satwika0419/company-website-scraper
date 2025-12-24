"""
TASK 2 — Company Profiling (Probiotics)

This file demonstrates how a simple, rule-based system
could identify and score a company's involvement in probiotics
using website text signals.

NOTE:
This is a conceptual implementation to demonstrate thinking
and logic, not production-grade ML or scraping code.
"""

PROBIOTICS_KEYWORDS = {
    "product_presence": [
        "probiotic", "lactobacillus", "bifidobacterium", "cfu", "strain"
    ],
    "scientific_rnd": [
        "clinical", "research", "study", "trial", "science", "r&d"
    ],
    "regulatory_quality": [
        "fssai", "fda", "efsa", "gmp", "iso", "certified", "compliance"
    ],
    "application_areas": [
        "gut health", "digestive health", "immunity",
        "animal nutrition", "veterinary", "human health"
    ],
    "commercial_intent": [
        "product", "manufacturing", "formulation",
        "supplier", "buy", "order", "distributor"
    ]
}


def detect_signals(text, keywords):
    """
    Detects keyword matches for a given category.
    """
    text = text.lower()
    return [kw for kw in keywords if kw in text]


def score_probiotics_involvement(website_text):
    """
    Scores a company's probiotics involvement
    based on observable website signals.
    """
    scores = {}
    total_score = 0

    for category, keywords in PROBIOTICS_KEYWORDS.items():
        matches = detect_signals(website_text, keywords)

        if len(matches) >= 3:
            score = 2  # strong signal
        elif len(matches) >= 1:
            score = 1  # weak/moderate signal
        else:
            score = 0  # no signal

        scores[category] = {
            "score": score,
            "matched_keywords": matches
        }

        total_score += score

    return total_score, scores


def classify_company(total_score):
    """
    Classifies the company based on total score.
    """
    if total_score >= 8:
        return "Strong Probiotics Player"
    elif total_score >= 4:
        return "Moderate / Adjacent Probiotics Player"
    else:
        return "Weak or Non-core Probiotics Involvement"


if __name__ == "__main__":
    # Example input text (normally from Task 1 scraper output)
    website_text = """
    We manufacture probiotic formulations for gut health and immunity.
    Our products contain clinically studied Lactobacillus strains.
    All manufacturing follows GMP and ISO standards.
    """

    total_score, detailed_scores = score_probiotics_involvement(website_text)
    classification = classify_company(total_score)

    print("Total Score:", total_score)
    print("Classification:", classification)
    print("\nDetailed Signal Breakdown:")
    for category, data in detailed_scores.items():
        print(f"- {category}: {data}")
