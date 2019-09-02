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

list = []
class Exercise5:
    def __init__(self, number, system):
        stringNumber = ""
        if system == 2:
            stringNumber = "Binary: "
        elif system == 16:
            stringNumber = "Hex: "
        else:
            print("Wrong system, please input again! ")
        list.clear()
        Exercise5.convert(number, system)
        for i in list:
            stringNumber += str(i)
        print(stringNumber)
    def convert(number, system):
        if int(number / system) > 0 or number % system != 0:
            Exercise5.convert(int(number / system), system)
            if number % system > 9:
                characters = ['A', 'B', 'C', 'D', 'E', 'F']
                list.append(characters[number % system - 10])
            else:
                list.append(number % system)