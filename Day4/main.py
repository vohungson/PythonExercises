print("Exercise Day4")

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
        numbers.sort()
        print(numbers)
        count = 0
        for i in range(len(numbers) - 1):
            if numbers[i] == numbers[i+1]:
                numbers[i] = 1000
                count += 1
        numbers.sort()
        for i in range(count):
            numbers.pop()
        print(numbers)


Exercise3([20, 20, 20, 30, 40, 50, 50, 50, 40])

# EXERCISE 4:
"""
Write a Python program to find the length of the longest consecutive 
elements sequence from a given unsorted array of integers.
Sample array: [49, 1, 3, 200, 2, 4, 70, 5] 
The longest consecutive elements sequence is [1, 2, 3, 4, 5], 
therefore the program will return its length 5.
"""


# EXERCISE 5:
"""
Write a Python program to find all the unique triplets such that sum of 
all the three elements [x, y, z (x ≤ y ≤ z)] equal to a specified number.
Sample array: [1, -2, 0, 5, -1, -4]
Target value: 2. 
"""


# EXERCISE 6:
"""
Write a Python program to compute the difference between two dates (year, months, days)
"""


# EXERCISE 7:
"""
Write a Python program to check whether a given number is an ugly number. 
In number system, ugly numbers are positive numbers whose only prime factors 
are 2, 3 or 5. First 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12. 
By convention, 1 is included. 
Test Date:Input an integer number: 235 
Expected Output :
It is not an ugly number.
"""


# EXERCISE 8:
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

# EXERCISE 9:
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

# EXERCISE 10:
"""
Write Python methods to calculate the area of a triangle. 
Expected Output:
Input Side-1: 10                                                                               
Input Side-2: 15                                                                               
Input Side-3: 20                                                                              
The area of the triangle is 72.6184377413890
"""