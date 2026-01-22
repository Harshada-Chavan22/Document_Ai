from rapidfuzz import process, fuzz
from data.dealer_master import DEALER_MASTER

def fuzzy_match_dealer(ocr_dealer_name, threshold=90):
    """
    Returns best matched dealer name and score
    """
    if not ocr_dealer_name:
        return None, 0.0

    match, score, _ = process.extractOne(
        ocr_dealer_name,
        DEALER_MASTER,
        scorer=fuzz.token_sort_ratio
    )

    if score >= threshold:
        return match, score / 100.0  # normalize to 0–1
    else:
        return None, score / 100.0
