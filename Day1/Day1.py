class Day:
    def exercise1(self):
        print("Exercise 1")
        print("Hello World")
        print("Vo Hung Son")
        print("Vietnamese")
        print(self)

class Exercise2:
    def __init__(self, x, y):
        print("Exercise 2")
        print("The sum of two numbers: ", x + y)
        print("Multiply of two numbers: ", x * y)
        print("The subtract of two numbers: ", x - y)
        print("The divide of two numbers: ", x / y)
        print("The remainder of two numbers: ", x % y)

class Exercise3:
    def __init__(self, a, b):
        print("\n")
        print("Exercise 3:")
        print("Area is", a, "*", b, "=", a * b)
        print("Perimeter is", 2, "* (", a, "+", b, ") =", 2 * (a + b))

class Exercise4:
    def __init__(self, fahrenheit):
        print("\nExercise 4:")
        celsius = (fahrenheit - 32) * 5 / 9
        print("The celcius degree is:", celsius)

