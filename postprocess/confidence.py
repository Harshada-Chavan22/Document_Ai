# postprocess/confidence.py
def compute_confidence(fields, vision):
    score = 1.0

    for key in ["model_name", "horse_power", "asset_cost"]:
        if fields.get(key) is None:
            score -= 0.2

    if not vision["signature"]["present"]:
        score -= 0.1
    if not vision["stamp"]["present"]:
        score -= 0.1

    return round(max(score, 0.0), 2)
