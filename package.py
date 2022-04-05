class Package(object):
    """Package details class."""

    def __init__(self, id, weight, distance_km, offer_code):
        self.id = id
        self.weight = weight or 0
        self.distance_km = distance_km or 0
        self.offer_code = offer_code or ''
        self.delivered = False
        self.discount_value = 0
        self.total_cost = 0
        self.estimated_delivery_time_in_hours = 0

def create_package_instance_list(package_args):
    package_details = []
    index = 0
    while index+4 <= len(package_args) and len(package_args) > 3:
        # pkg_id1, pkg_weight1_in_kg, distance1_in_km, offer_code1
        package_details.append(
            Package(package_args[index], package_args[index+1], package_args[index+2], package_args[index+3]))
        index += 4
    # Sort the package details with heaviest wieght firt.
    package_details.sort(key=lambda x:x.weight, reverse=True)
    return package_details
