class Vehicle(object):
    """Vehicle class."""

    def __init__(self, id, hrs=0):
        self.id = id
        self.hrs = 0


def create_vehicle_list(no_of_vehicles):
    return [Vehicle(index)
            for index in range(1,no_of_vehicles+1)]


def get_current_vehicle(vehicle_trip_details):
    """Get current vehicle for trip with minimum travel time."""
    if not vehicle_trip_details:
        return None
    min_trip_hrs_vehicle = None
    for vehicle in vehicle_trip_details:
        if not min_trip_hrs_vehicle:
            min_trip_hrs_vehicle = vehicle
            continue
        if  min_trip_hrs_vehicle.hrs > vehicle.hrs:
            min_trip_hrs_vehicle = vehicle
    return min_trip_hrs_vehicle