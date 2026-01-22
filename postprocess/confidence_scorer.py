def compute_document_confidence(ocr_lines, fields):
    """
    Returns document-level confidence between 0 and 1
    """

    score = 0.0
    weight_sum = 0.0

    # 1️⃣ Dealer fuzzy match score
    if fields.get("dealer_match_score") is not None:
        score += fields["dealer_match_score"] * 0.25
        weight_sum += 0.25

    # 2️⃣ OCR confidence (average)
    if ocr_lines:
        avg_ocr_conf = sum(l["confidence"] for l in ocr_lines) / len(ocr_lines)
        score += avg_ocr_conf * 0.25
        weight_sum += 0.25

    # 3️⃣ Field completeness
    required_fields = ["dealer_name", "model_name", "horse_power", "asset_cost"]
    present = sum(1 for f in required_fields if fields.get(f) is not None)
    completeness = present / len(required_fields)
    score += completeness * 0.25
    weight_sum += 0.25

    # 4️⃣ Signature presence
    if fields.get("signature", {}).get("present"):
        score += 0.125
        weight_sum += 0.125

    # 5️⃣ Stamp presence
    if fields.get("stamp", {}).get("present"):
        score += 0.125
        weight_sum += 0.125

    # Normalize
    if weight_sum > 0:
        score /= weight_sum

    return round(score, 3)
