import datetime
import re

# EXERCISE 1:
"""
Write a Python program to find the number of even and odd integers in a given array of integers.
"""


class Exercise1:
    def __init__(self, numbers):
        print("\nExercise 1: ")
        even = 0
        odd = 0
        for n in numbers:
            if n % 2 == 0:
                even += 1
            else:
                odd += 1
        print("Number of even integers: ", even)
        print("Number of odd integers: ", odd)


Exercise1([10, 11, 21, 45, 56, 84, 25, 32, 57, 46, 83, 8, 5, 4, 7, 6, 3, 41, 23, 72])

# EXERCISE 2:
"""
Write a Python program to check if the sum of all the 10's in the array is exactly 30. 
Return false if the condition does not satisfy, otherwise true. 
"""


class Exercise2:
    def __init__(self, numbers):
        print("\nExercise 2: ")
        print(numbers)
        print(Exercise2.check_ten_numbers(numbers))

    @staticmethod
    def check_ten_numbers(numbers):
        check = True
        sum_num = 0
        for n in numbers:
            sum_num += n
        if sum_num != 30:
            check = False
        return check


Exercise2([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

# EXERCISE 3:
"""
Write a Python program to remove the duplicate elements of a given array 
and return the new length of the array.
Sample array: [20, 20, 30, 40, 50, 50, 50]
After removing the duplicate elements the program 
should return 4 as the new length of the array. 
"""


class Exercise3:
    def __init__(self, numbers):
        print("\nExercise 3: ")
        numbers.sort ()
        print ( numbers )
        count = 0
        for i in range ( len ( numbers ) - 1 ):
            if numbers[i] == numbers[i + 1]:
                numbers[i] = 1000
                count += 1
        numbers.sort ()
        for i in range ( count ):
            numbers.pop ()
        print ( numbers )


Exercise3 ( [20, 20, 20, 30, 40, 50, 50, 50, 40] )

# EXERCISE 4:
"""
Write a Python program to find the length of the longest consecutive 
elements sequence from a given unsorted array of integers.
Sample array: [49, 1, 3, 200, 2, 4, 70, 5] 
The longest consecutive elements sequence is [1, 2, 3, 4, 5], 
therefore the program will return its length 5.
"""


class Exercise4:
    def __init__(self, numbers):
        print ( "\nExercise 4: " )
        numbers.sort ()
        print ( numbers )
        start_longest = end_longest = start = end = count = 0
        for i in range ( len ( numbers ) - 1 ):
            if numbers[i] + 1 == numbers[i + 1]:
                end += 1
                if end - start > end_longest - start_longest:
                    start_longest = start
                    end_longest = end
            else:
                start = end = i + 1
        print ( "start longest:", start_longest )
        print ( "end longest:", end_longest )
        print ( "Output:", numbers[start_longest:end_longest + 1] )


Exercise4 ( [49, 1, 3, 200, 2, 4, 70, 5, 11, 12, 13, 14, 15, 16, 20] )

# EXERCISE 5:
"""
Write a Python program to compute the difference between two dates (year, months, days)
"""

print("\nExercise 5")
x = datetime.datetime(2020, 5, 17)
y = datetime.datetime(2010, 6, 13)
z = x - y
print(z)


# EXERCISE 6:
"""
Write a Python method to find the smallest number among three numbers. 
Go to the editor
Test Data:
Input the first number: 25
Input the Second number: 37
Input the third number: 29 
Expected Output:
The smallest value is 25.0
"""


class Exercise6:
    def __init__(self, numbers):
        print("\nExercise 6: ")
        numbers.sort()
        print("The smallest value is", numbers[0])


Exercise6([25, 37, 29])


# EXERCISE 7:
"""
Write a Python method to check whether a string is a valid password. Go to the editor
Password rules:
A password must have at least ten characters.
A password consists of only letters and digits.
A password must contain at least two digits.
Expected Output:
1. A password must have at least eight characters.                                             
2. A password consists of only letters and digits.                                         
3. A password must contain at least two digits                                        
Input a password (You are agreeing to the above Terms and Conditions.): abcd1234           
Password is valid: abcd1234
"""


class Exercise7:
    def __init__(self, string):
        print("\nExercise 7: ")
        print("The password is: ", Exercise7.check_password(string))

    @staticmethod
    def check_password(string):
        check = True
        x = re.findall("[a-zA-Z0-9]", string)
        d = re.findall("[\d]", string)
        if len(string) != len(x) or len(x) < 8 or len(d) < 2:
            check = False
        return check


Exercise7("abcdefg12")


# EXERCISE 8:
"""
Write Python methods to calculate the area of a triangle. 
Expected Output:
Input Side-1: 10                                                                               
Input Side-2: 15                                                                               
Input Side-3: 20                                                                              
The area of the triangle is 72.6184377413890
"""


class Exercise8:
    def __init__(self, a, b, c):
        print("\nExercise 8: ")
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("Area =", area)


Exercise8(10, 15, 20)
