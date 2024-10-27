import pytest
from apis import get_gas_price, get_power_price
from tests.conftest import mileages

"""
# test function
@pytest.mark.parametrize('a,b,result', [(1,6,7),(5,10,15),(6,12,18)])
def test_sum(a, b, result):
    res = a + b
    assert res == result
"""

class TestAPI:
    @pytest.mark.parametrize('function', [get_gas_price, get_power_price])
    def test_get_price(self, function):
        res = function()
        assert isinstance(res, int) or isinstance(res, float)

class TestCar:
    @pytest.mark.parametrize('service_cost, insurance_cost', [(20, 40), (20000, 45000)])
    def test_static_year_cost(self, car, service_cost, insurance_cost):
        res = car.static_year_cost()
        expected = car.service_cost + car.insurance_cost
        assert res == expected

    @pytest.mark.parametrize('mileage', mileages)
    def test_dynamic_year_cost(self, car, mileage):
        res = car.dynamic_year_cost(mileage)
        expected = car.fuel_economy * mileage / 100 * get_gas_price()
        assert res == expected

class TestElectricCar:
    @pytest.mark.parametrize('mileage', mileages)
    def test_dynamic_year_cost(self, electric_car, mileage):
        res = electric_car.dynamic_year_cost(mileage)
        expected = electric_car.power_consumption * mileage / 1000 * get_power_price()
        assert res == expected

class TestCalculator:
    def test_add_car(self, calculator, car):
        calculator.add_car(car)
        assert calculator.cars
        assert car in calculator.cars
        assert calculator.cars[car] > 0

    def test_print_cars(self, calculator):
        calculator.print_cars()

    def test_get_left_price(self, calculator, car):
        res = calculator.get_left_price(car)
        init_price = car.price
        for _ in range(calculator.years):
            init_price -= init_price * calculator.year_loss
        assert res == init_price