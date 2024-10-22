import calculator

if __name__ == '__main__':
    calc = calculator.Calculator(years=3)
    calc.add_car(
        calculator.Car("Toyota", 30000, 7, 1200, 2500)
    )
    calc.add_car(
        calculator.ElectricCar("Tesla", 200000, 0, 0, 5500, 150)
    )
    calc.add_car(
        calculator.Car("Range Rover", 650000, 15, 20000, 45000)
    )

    calc.print_cars()
