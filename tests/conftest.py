import pytest
from calculator import Car, ElectricCar, Calculator

# test parameters for mileage in tests
mileages = [100, 10000, 30000, 450000]

# test gasoline car
@pytest.fixture
def car():
    print('\n Creating a new gasoline car...\n')
    return Car("BMW", 1750000, 15,
               20000, 45000)

# test electric car
@pytest.fixture
def electric_car():
    print('\n Creating a new electric car...\n')
    return ElectricCar("Tesla", 200000, 0,
                           0, 5500, 150)

# test Calculator class
@pytest.fixture
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return  res