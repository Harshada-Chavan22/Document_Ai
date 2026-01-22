import re
from extraction.dealer_matcher import fuzzy_match_dealer

def extract_fields(ocr_lines):
    fields = {
        "dealer_name": None,
        "dealer_match_score": 0.0,
        "model_name": None,
        "horse_power": None,
        "asset_cost": None
    }

    raw_dealer_name = None

    for line in ocr_lines:
        text = line["text"]
        text_lower = text.lower()

        # Dealer (raw)
        if "dealer" in text_lower and raw_dealer_name is None:
            raw_dealer_name = text.split(":", 1)[-1].strip()

        # Model
        if "model" in text_lower and fields["model_name"] is None:
            fields["model_name"] = text.split(":", 1)[-1].strip()

        # Horse Power
        hp_match = re.search(r"(\d+)\s*hp", text_lower)
        if hp_match and fields["horse_power"] is None:
            fields["horse_power"] = int(hp_match.group(1))

        # Asset Cost
        cost_match = re.search(r"\b\d{4,}\b", text)
        if ("cost" in text_lower or "total" in text_lower) and cost_match:
            fields["asset_cost"] = int(cost_match.group())

    # 🔹 Fuzzy match dealer
    if raw_dealer_name:
        matched_name, score = fuzzy_match_dealer(raw_dealer_name)
        fields["dealer_name"] = matched_name or raw_dealer_name
        fields["dealer_match_score"] = score

    return fields
