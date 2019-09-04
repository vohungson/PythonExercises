print("Python Exercise - Day 3")


# EXERCISE 1: Print the all characters between two positions of a string


class Exercise1:
    def __init__(self, start, end, string):
        print("\nExercise 1: ")
        print("The all characters between two positions of a string: ", end='')
        for char in string[start:end]:
            print(char, end='')


Exercise1(5, 15, "Print the all characters")

# EXERCISE 2: Reverse vowels in a given string
'''
=> Replace the character from the index in the string
def change_char(string, index, character):
    return string[:index] + character + string[index+1:]
'''


class Exercise2:
    def __init__(self, string):
        print("\n\nExercise 2: ")
        string_vowel = ""
        for char in string:
            c = char.lower()
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                string_vowel += char
        j = len(string_vowel) - 1
        for i in range(len(string)):
            c = string[i].lower()
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                string = string[:i] + string_vowel[j] + string[(i + 1):]
                j -= 1
        print(string)


Exercise2("Reverse vowels in a given string.")


# EXERCISE 3: Convert all characters of a string into Lower case


class Exercise3:
    def __init__(self, string):
        print("\nExercise 3: ")
        print(string.lower())


Exercise3("CONVERT ALL CHARACTERS OF A STRING")


# EXERCISE 4: Find the k largest elements in a given array.
# Elements in the array can be in any order


class Exercise4:
    def __init__(self):
        print("\nExercise 4: Find the k largest elements in a given array")
        numbers = [7, 3, 2, 10, 4, 9, 8, 6, 0, 10]
        largest_number = 0
        for x in numbers:
            if x > largest_number:
                largest_number = x
        print("The largest number is: ", largest_number)
        count = 0
        for x in numbers:
            if x == largest_number:
                count += 1
        if count == 1:
            print(count, "largest element", largest_number)
        else:
            print(count, "largest elements", largest_number)


Exercise4()


# EXERCISE 5: Find the numbers greater than
# the average of the numbers of a given array


class Exercise5:
    def __init__(self, numbers):
        print("\nExercise 5: ")
        average = numbers[int(len(numbers) / 2)]
        for n in numbers:
            if n > average:
                print(n, end=' ')


Exercise5([7, 3, 2, 1, 9, 4, 8, 6, 0, 10])


# EXERCISE 6: Create the concatenation of the two strings
# except removing the first character of each string.
# The length of the strings must be 1 and above. 

class Exercise6:
    def __init__(self, string1, string2):
        print("\n\nExercise 6: ")
        string3 = string1[1:] + string2[1:]
        print("Output:")
        print(string3)


Exercise6("Python", "Tutorial")


# EXERCISE 7: Find the total number of continuous subarrays
# in a given array of integers whose sum equals to a given integer.


class Exercise7:
    def __init__(self, numbers, k):
        print("\nExercise 7: ")
        count = 0
        i = 0
        while i < len(numbers):
            sum_nums = 0
            j = 0
            for m in numbers[i:]:
                sum_nums += m
                if sum_nums == k:
                    count += 1
                    i += j
                    break
                j += 1
            i += 1
        print("Number of contiuous subarrays: ", count)


Exercise7([4, 2, 3, 3, 3, 7, 2, 4], 6)


# EXERCISE 8: Write a Java program to get the position
# of a prime number which is near to the given integer.

class Exercise8:
    def __init__(self, prime):
        print("\nExercise 8: ")
        print("List of prime numbers: ")
        position = 0
        for n in range(2, prime + 1):
            if Exercise8.check_prime(n):
                print(n, end=' ')
                position += 1
        print("\nPosition: ", position)

    @staticmethod
    def check_prime(number):
        check = True
        for n in range(2, number):
            if number % n == 0:
                check = False
                break
        return check


Exercise8(13)

# EXERCISE 9:
"""
Write a Java program to return the sum of the numbers 
(may form more than one digits), appearing in the string.
         Sample Output:
         The given string is: it 15 is25 a 20string
         The sum of numbers in the string is: 60
"""
import re


class Exercise9:
    def __init__(self, string):
        print("\nExercise 9:")
        x = re.findall("\d+", string)
        print(x)
        sum_num = 0
        for n in x:
            sum_num += int(n)
        print("The sum of numbers in the string is: ", sum_num)


Exercise9("it 15 is25 a 20string")

# EXERCISE 10:
"""
Write a Java program to count the number of words ending in 'm' or 'n' (not case sensitive).
         Sample Output:
         The given string is: mam is in the room
         The number of words ends either m or n is: 3
"""


class Exercise10:
    def __init__(self, string):
        print("\nExercise 10: ")
        string += '.'
        x = re.findall("[\w]*[m|n][\W]", string)
        print(x)
        print("The number of words:", len(x))


Exercise10("mam is in the room")


# EXERCISE 11: