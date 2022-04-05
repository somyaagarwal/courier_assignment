"""Module for courier service."""

from package import Package
import package as package_class
from package_discount import PackageDiscount
from vehicle import Vehicle
import vehicle

WIGHT_COST = 10
DISTANCE_COST = 5
NO_OF_PACKAGE_DETAILS = 4 

discounts = {
    'OFR001': PackageDiscount('OFR001', 0, 200, 70, 200, 10),
    'OFR002': PackageDiscount('OFR002', 50, 150, 100, 250, 7),
    'OFR003': PackageDiscount('OFR003', 50, 250, 10, 150, 5)
}

def calculate_total_delivery_cost( base_delivery_cost, no_of_packages, *package_args):
    """Calculates the total cost of the package delivery.

    Args:
        base_delivery_cost: (int) Base delivery cost.
        no_of_packages: (int) Number of packages to be delivered.
        package_args: Package details list.
        
    Returns:
        A list of tuple of package ID, package discount and cost."""
    if len(package_args) / NO_OF_PACKAGE_DETAILS != no_of_packages:
        return 'Insufficient Number of package arguments' 
    package_details = package_class.create_package_instance_list(package_args)

    for package in package_details:
        cost_without_discount = _calculate_total_cost(base_delivery_cost, package)
        discount = _calculate_discount(package)
        package.discount_value = cost_without_discount * discount / 100
        package.total_cost = cost_without_discount - package.discount_value
    return [(package.id, package.discount_value, package.total_cost)
            for package in package_details]

def calculate_delivery_time_estimation(base_delivery_cost, no_of_packages,
    no_of_vehicles, max_speed, max_carriable_weight, *package_args):
    """Calcualtes the total cost of the package delivery.

    Args:
        base_delivery_cost: (int) Base delivery cost.
        no_of_packages: (int) Number of packages to be delivered.
        no_of_vehicles: (int) Total available vehicles.
        max_speed: (int)Max speed of vehicle.
        max_carriable_weight: (int) Maximum weight in Kg.
        package_args: Package details list.
        
    Returns:
        A list of tuple of package ID, package discount, cost and delivery estimate."""
    if len(package_args) / NO_OF_PACKAGE_DETAILS != no_of_packages:
        return 'Insufficient Number of package arguments' 
    package_details = package_class.create_package_instance_list(package_args)
    vehicle_trip_details = vehicle.create_vehicle_list(no_of_vehicles)
    current_vehicle = vehicle_trip_details[0]
    total_cost = 0
    delivered_packages = []
    while len(delivered_packages) < len(package_details):
        current_trip_time = []
        current_packages = _select_packages_for_delivery_trip(package_details, no_of_vehicles, max_carriable_weight)
        
        for package in current_packages:
            cost_without_discount = _calculate_total_cost(base_delivery_cost, package)
            discount = _calculate_discount(package)
            package.discount_value = cost_without_discount * discount / 100
            package.total_cost = cost_without_discount - package.discount_value
            package.estimated_delivery_time_in_hours = current_vehicle.hrs + round(package.distance_km / float(max_speed),2)
            current_trip_time.append(package.estimated_delivery_time_in_hours)
            # Set delivery status so that the smae package is not selected again for delivery.
            package.delivered = True
            delivered_packages.append(package)
        current_vehicle.hrs = max(current_trip_time) * 2  # Time taken for round trip.
        current_vehicle = vehicle.get_current_vehicle(vehicle_trip_details)
    return [
        (package.id, package.discount_value, package.total_cost,
         package.estimated_delivery_time_in_hours)
        for package in package_details]

def _calculate_total_cost(base_delivery_cost, package):
    """Calculates total cost of the package without discount.

    Args:
        package: Package Instance.
        base_delivery_cost: (int) Base cost.
        
    Returns:
        Package Instance list."""
    return base_delivery_cost + (package.weight * WIGHT_COST) + (
        package.distance_km * DISTANCE_COST)

def _calculate_discount(package):
    """Calculates discount on the given package.

    Args:
        package: Package Instance.
        
    Returns:
        Discount value."""
    offer_details = discounts.get(package.offer_code)
    discount = 0
    if not offer_details:
        return discount
    if all([
        package.distance_km >= offer_details.min_distance_km,
        package.distance_km <= offer_details.max_distance_km,
        package.weight >= offer_details.min_weight_kg,
        package.weight <= offer_details.max_weight_kg]):
        discount = offer_details.discount
    return discount

def _select_packages_for_delivery_trip(packages, vehicles_available, max_load):
    """Returns delivery packages for one trip.
    
    Args:
        packages: Package Instance list.
        vehicles_available: (int) Total available vehicles.
        max_load: (int) Maximum weight in Kg.
        
    Returns:
        Package Instance list."""
    total_weight = 0
    package_index = 0
    # Selected packages with weight as key and packages as value.
    selected_packages = {}
    current_packages = []
    while package_index<len(packages) and total_weight <= max_load:
        for package in packages[package_index:]:
            if not package.delivered:
                if total_weight + package.weight <= max_load:
                    total_weight += package.weight
                    current_packages.append(package)
        selected_packages[total_weight] = current_packages
        current_packages = []
        total_weight = 0
        package_index += 1
    
    # Return the selected package with maximum weight.
    return selected_packages[(max(selected_packages.keys()))]


    