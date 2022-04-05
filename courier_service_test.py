import courier_service
from courier_result import CourierResult
import courier_result
from package import Package
import unittest

class CourierService(unittest.TestCase):

    def setUp(self):
        self.package1 = Package(id='PKG1', weight=5, distance_km=5, offer_code='OFR001')
        self.package2 = Package(id='PKG2', weight=15, distance_km=5, offer_code='OFR002')
        self.package3 = Package(id='PKG3', weight=10, distance_km=100, offer_code='OFR003')
        self.package4 = Package(id='PKG4', weight=110, distance_km=60, offer_code='OFR002')
        self.package5 = Package(id='PKG5', weight=155, distance_km=95, offer_code='NA')

    def test_get_delivery_cost(self):
        expected_result = CourierResult(
            id=self.package1.id, discounted_value=0, total_cost=175)

        response = courier_service.calculate_total_delivery_cost(
            100, 1, self.package1.id, self.package1.weight,
            self.package1.distance_km, self.package1.offer_code)
        
        self.assertTrue(len(response))
        actual_result = courier_result.get_courier_cost_result_list(response)
        self.assertEqual(actual_result[0].discounted_value, expected_result.discounted_value)
        self.assertEqual(actual_result[0].total_cost, expected_result.total_cost)

    def test_get_delivery_cost_with_multiple_packages(self):

        expected_result_pkg1 = CourierResult(
            id=self.package1.id, discounted_value=0, total_cost=175)
        expected_result_pkg2 = CourierResult(
            id=self.package2.id, discounted_value=0, total_cost=275)
        expected_result_pkg3 = CourierResult(
            id=self.package3.id, discounted_value=35, total_cost=665)

        response = courier_service.calculate_total_delivery_cost(
            100, 3,
            'PKG1', 5, 5, 'OFR001',
            'PKG2', 15, 5, 'OFR002',
            'PKG3', 10, 100, 'OFR003')

        self.assertTrue(len(response))
        actual_result = courier_result.get_courier_cost_result_list(response)
        for result in actual_result:
            if result.id == expected_result_pkg1.id:
                self.assertEqual(result.discounted_value, expected_result_pkg1.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg1.total_cost)
            if result.id == expected_result_pkg2.id:
                self.assertEqual(result.discounted_value, expected_result_pkg2.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg2.total_cost)
            if result.id == expected_result_pkg3.id:
                self.assertEqual(result.discounted_value, expected_result_pkg3.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg3.total_cost)


    def test_delivery_time_estimation(self):
        result = courier_service.calculate_delivery_time_estimation(
            100, 1, 2, 70, 200, 'PKG1', 50, 30, 'OFR001')
        self.assertTrue(len(result))


    def test_delivery_time_estimation_with_multiple_packages(self):

        expected_result_pkg1 = CourierResult(
            id=self.package1.id, discounted_value=0, total_cost=750, estimated_delivery_time_in_hours=4.01)
        expected_result_pkg2 = CourierResult(
            id=self.package2.id, discounted_value=0, total_cost=1475, estimated_delivery_time_in_hours=1.78)
        expected_result_pkg3 = CourierResult(
            id=self.package3.id, discounted_value=0, total_cost=2350, estimated_delivery_time_in_hours=1.42)
        expected_result_pkg4 = CourierResult(
            id=self.package4.id, discounted_value=105, total_cost=1395, estimated_delivery_time_in_hours=0.85)
        expected_result_pkg5 = CourierResult(
            id=self.package5.id, discounted_value=0, total_cost=2125, estimated_delivery_time_in_hours=4.22)

        response = courier_service.calculate_delivery_time_estimation(
             100, 5, 2, 70, 200,
            'PKG1', 50, 30, 'OFR001',
            'PKG2', 75, 125,'OFR008',
            'PKG3', 175, 100, 'OFR003',
            'PKG4', 110, 60, 'OFR002',
            'PKG5', 155, 95, 'OFR0011')

        self.assertTrue(len(response))
        actual_result = courier_result.get_courier_delviery_estimate_result_list(response)
        for result in actual_result:
            if result.id == expected_result_pkg1.id:
                self.assertEqual(result.discounted_value, expected_result_pkg1.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg1.total_cost)
                self.assertAlmostEqual(result.estimated_delivery_time_in_hours, expected_result_pkg1.estimated_delivery_time_in_hours, 1)
            if result.id == expected_result_pkg2.id:
                self.assertEqual(result.discounted_value, expected_result_pkg2.discounted_value)
                self.assertAlmostEqual(result.estimated_delivery_time_in_hours, expected_result_pkg2.estimated_delivery_time_in_hours, 1)
                self.assertEqual(result.total_cost, expected_result_pkg2.total_cost)
            if result.id == expected_result_pkg3.id:
                self.assertEqual(result.discounted_value, expected_result_pkg3.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg3.total_cost)
                self.assertAlmostEqual(result.estimated_delivery_time_in_hours, expected_result_pkg3.estimated_delivery_time_in_hours, 1)
            if result.id == expected_result_pkg4.id:
                self.assertEqual(result.discounted_value, expected_result_pkg4.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg4.total_cost)
                self.assertAlmostEqual(result.estimated_delivery_time_in_hours, expected_result_pkg4.estimated_delivery_time_in_hours, 1)
            if result.id == expected_result_pkg5.id:
                self.assertEqual(result.discounted_value, expected_result_pkg5.discounted_value)
                self.assertEqual(result.total_cost, expected_result_pkg5.total_cost)
                self.assertAlmostEqual(result.estimated_delivery_time_in_hours, expected_result_pkg5.estimated_delivery_time_in_hours, 1)


if __name__ == '__main__':
    unittest.main()