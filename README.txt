This package contains the courier service calcuations
for getting the cost of courier package and the estimated time for its delivery


Usage:
The code is written in python. To run it install python3

For calulating cost
python3 -c "import courier_service; print(courier_service.calculate_total_delivery_cost(100,3,'PKG1', 5, 5, 'OFR001', 'PKG2', 15, 5, 'OFR002','PKG3', 10, 100, 'OFR003'))"

For calulating estimated time and cost:
python3 -c "import courier_service; print(courier_service.calculate_delivery_time_estimation(100,3,2,70,200,'PKG1', 50, 30, 'OFR001', 'PKG2', 75, 125, 'OFR008','PKG3', 175, 100, 'OFR003','PKG4', 110, 60, 'OFR002','PKG5', 155, 95, 'OFR0011'))"
[('PKG2', 0, 1475, 1.79), ('PKG3', 0, 2350, 1.43), ('PKG4', 105, 1395, 0.86), ('PKG1', 0, 750, 4.01), ('PKG5', 0, 2125, 4.22)]