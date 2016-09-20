import Calculator
import time

calc = Calculator.Calculator

# Doing some calulations with our calc object
print("1 + 1 is " + str(calc.add(1,1)))

print("3 - 2 is " + str(calc.sub(3,2)))

print("4 * 4 is " + str(calc.multiply(4,4)))

print("4 / 2 is " + str(calc.division(4,2)))

print("3 ** 2 is " + str(calc.toThePowerOf(3,2)))
