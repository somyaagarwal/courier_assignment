class PackageDiscount(object):
    """Package discount class."""

    def __init__(self, id, min_distance_km, max_distance_km, min_weight_kg, max_weight_kg, discount):
        self.id = id
        self.min_weight_kg = min_weight_kg or 0
        self.max_weight_kg = max_weight_kg or 0
        self.min_distance_km = min_distance_km or 0
        self.max_distance_km = max_distance_km or 0
        self.discount = discount or 0
