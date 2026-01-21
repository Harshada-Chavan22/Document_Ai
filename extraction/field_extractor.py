import re

def extract_fields(ocr_lines):
    fields = {
        "dealer_name": None,
        "model_name": None,
        "horse_power": None,
        "asset_cost": None
    }

    for line in ocr_lines:
        text = line["text"].lower()

        # Dealer Name
        if "dealer" in text and fields["dealer_name"] is None:
            fields["dealer_name"] = line["text"].split(":", 1)[-1].strip()

        # Model Name
        if "model" in text and fields["model_name"] is None:
            fields["model_name"] = line["text"].split(":", 1)[-1].strip()

        # Horse Power
        hp_match = re.search(r"(\d+)\s*hp", text)
        if hp_match and fields["horse_power"] is None:
            fields["horse_power"] = int(hp_match.group(1))

        # Asset Cost
        cost_match = re.search(r"\b\d{4,}\b", text)
        if ("cost" in text or "total" in text) and cost_match:
            fields["asset_cost"] = int(cost_match.group())

    return fields
