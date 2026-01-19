# postprocess/validation.py
def validate_fields(dealer, model, hp, cost, vision):
    return {
        "dealer_name": dealer,
        "model_name": model,
        "horse_power": hp,
        "asset_cost": cost,
        "signature": vision["signature"],
        "stamp": vision["stamp"]
    }
