print("Exercises of Day1")
import Day1

# Exercise 1:
'''
Print 'Hello World' on screen and then print your full name and your nationality.
Expected Output :
Hello World
Vo Hung Son, Vietnamese.
'''
Day1.Day.exercise1("\n")

# Exercise 2:
'''
Print the sum, multiply, subtract, divide 
and remainder of two numbers taken from the user input.
'''
Day1.Exercise2(19, 12)

# Exercise 3:
'''
Take width and height of a rectangle and print the area and perimeter.
Test: Width = 5 Height = 8
Expected Output: Area is 5 * 8 = 40; Perimeter is 2 * (5 + 8) = 26
'''
Day1.Exercise3(5, 8)

# Exercise 4:
'''
Print the result of Converting temperature from Fahrenheit to Celsius degree
'''
Day1.Exercise4(41)

# Exercise 5:
'''
Convert from integer to hex and binary presentation.
         Test:
         Integer = 10
         Output:
         Binary: 1010
         Hex: A
'''
print("\nExercise 5: ")
Day1.Exercise5(10, 2)
Day1.Exercise5(10, 16)

# Exercise 6: Print the current time in GMT.
print("\nExercise 6: ")
import datetime
x = datetime.datetime.now()
print(x)

# Exercise 7: Take a number from user and check whether it is negative or positive
print("\nExercise 7: ")
number = 7
if number >= 0:
    print("This number is positive")
else:
    print("This number is negative")

# Exercise 8: Take 10 numbers from user and print the largest, smallest and medium value
print("\nExercise 8: ")
numbers = [3, 4, 8, 1, 9, 2, 5, 7, 10, 6]
numbers.sort()
print("smallest value:", numbers[0])
print("largest value:", numbers[len(numbers) - 1])
print("medium value:", numbers[int(len(numbers)/2)])
