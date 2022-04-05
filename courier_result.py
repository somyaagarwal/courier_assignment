class CourierResult(object):
    """Courier result class for evaluating tests outcome."""

    def __init__(self, id, discounted_value=0, total_cost=0, estimated_delivery_time_in_hours=0):
        self.id = id or 0
        self.discounted_value = discounted_value
        self.total_cost = total_cost
        self.estimated_delivery_time_in_hours = estimated_delivery_time_in_hours

def get_courier_cost_result_list(details):
    """Returns the cost result list."""
    return [CourierResult(detail[0], detail[1], detail[2]) for detail in details]

def get_courier_delviery_estimate_result_list(details):
    """Returns the delivery estimate result list."""
    return [CourierResult(detail[0], detail[1], detail[2], detail[3]) for detail in details]